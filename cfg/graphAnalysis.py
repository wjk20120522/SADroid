#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.sax.saxutils import escape

from androguard.core import bytecode
from androguard.core.bytecodes.dvm_permissions import DVM_PERMISSIONS
from androguard.core.analysis.risk import PERMISSIONS_RISK, \
    INTERNET_RISK, PRIVACY_RISK, PHONE_RISK, SMS_RISK, MONEY_RISK

from copy import deepcopy


class Graph(object):

    def __init__(self):
        """
        Initialize a graph with edges, name, graph attributes.
        """
        self.graph = {}  # dictionary for graph attributes
        self.node = {}  # empty node dict (created before convert)
        self.adj = {}  # empty adjacency dict
        self.edge = self.adj

    @property
    def name(self):
        return self.graph.get('name', '')

    @name.setter
    def name(self, s):
        self.graph['name'] = s

    def __str__(self):
        """
        Return the graph name.
        """
        return self.name

    def __iter__(self):
        """
        Iterate over the nodes. Use the expression 'for n in G'.
        """
        return iter(self.node)

    def __contains__(self, n):
        """
        Return True if n is a node, False otherwise. Use the expression
        """
        try:
            return n in self.node
        except TypeError:
            return False

    def __len__(self):
        """
        Return the number of nodes. Use the expression 'len(G)'.
        """
        return len(self.node)

    def __getitem__(self, n):
        """
        Return a dict of neighbors of node n.  Use the expression 'G[n]'.
        """
        return self.adj[n]

    def add_node(self, n, attr_dict=None, **attr):
        """
        Add a single node n and update node attributes.
        """
        # set up attribute dict

        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dictionary.')
        if n not in self.node:
            self.adj[n] = {}
            self.node[n] = attr_dict
        else:
            # update attr even if node already exists
            self.node[n].update(attr_dict)

    def add_nodes_from(self, nodes, **attr):
        """
        Add multiple nodes.
        """

        for n in nodes:
            try:
                newnode = n not in self.node
            except TypeError:
                (nn, ndict) = n
                if nn not in self.node:
                    self.adj[nn] = {}
                    newdict = attr.copy()
                    newdict.update(ndict)
                    self.node[nn] = newdict
                else:
                    olddict = self.node[nn]
                    olddict.update(attr)
                    olddict.update(ndict)
                continue
            if newnode:
                self.adj[n] = {}
                self.node[n] = attr.copy()
            else:
                self.node[n].update(attr)

    def remove_node(self, n):
        """
        Remove node n.
        """

        adj = self.adj
        try:
            nbrs = list(adj[n].keys())  # keys handles self-loops (allow mutation later)
            del self.node[n]
        except KeyError:
            # NetworkXError if n not in self
            raise NetworkXError('The node %s is not in the graph.' % (n, ))
        for u in nbrs:
            del adj[u][n]  # remove all edges n-u in graph
        del adj[n]  # now remove node

    def remove_nodes_from(self, nodes):
        """
        Remove multiple nodes.
        """

        adj = self.adj
        for n in nodes:
            try:
                del self.node[n]
                for u in list(adj[n].keys()):  # keys() handles self-loops
                    del adj[u][n]  # (allows mutation of dict in loop)
                del adj[n]
            except KeyError:
                pass

    def nodes_iter(self, data=False):
        """
        Return an iterator over the nodes.
        """
        if data:
            return iter(self.node.items())
        return iter(self.node)

    def nodes(self, data=False):
        """
        Return a list of the nodes in the graph.
        """

        return list(self.nodes_iter(data))

    def number_of_nodes(self):
        """
        Return the number of nodes in the graph.
        """

        return len(self.node)

    def order(self):
        """
        Return the number of nodes in the graph.
        """

        return len(self.node)

    def has_node(self, n):
        """
        Return True if the graph contains the node n.
        """

        try:
            return n in self.node
        except TypeError:
            return False

    def add_edge(self, u, v, attr_dict=None, **attr):
        # set up attribute dictionary

        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dictionary.'
                                    )

        # add nodes

        if u not in self.node:
            self.adj[u] = {}
            self.node[u] = {}
        if v not in self.node:
            self.adj[v] = {}
            self.node[v] = {}

        # add the edge

        datadict = self.adj[u].get(v, {})
        datadict.update(attr_dict)
        self.adj[u][v] = datadict
        self.adj[v][u] = datadict

    def add_edges_from(self, ebunch, attr_dict=None, **attr):
        """
        Add all the edges in ebunch.
        """

        # set up attribute dict

        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dictionary.')

        # process ebunch

        for e in ebunch:
            ne = len(e)
            if ne == 3:
                (u, v, dd) = e
            elif ne == 2:
                (u, v) = e
                dd = {}
            else:
                raise NetworkXError('Edge tuple %s must be a 2-tuple or 3-tuple.'
                                     % (e, ))
            if u not in self.node:
                self.adj[u] = {}
                self.node[u] = {}
            if v not in self.node:
                self.adj[v] = {}
                self.node[v] = {}
            datadict = self.adj[u].get(v, {})
            datadict.update(attr_dict)
            datadict.update(dd)
            self.adj[u][v] = datadict
            self.adj[v][u] = datadict

    def remove_edge(self, u, v):
        """
        Remove the edge between u and v.
        """

        try:
            del self.adj[u][v]
            if u != v:  # self-loop needs only one entry removed
                del self.adj[v][u]
        except KeyError:
            raise NetworkXError('The edge %s-%s is not in the graph'
                                % (u, v))

    def remove_edges_from(self, ebunch):
        """
        Remove all edges specified in ebunch.
        """

        adj = self.adj
        for e in ebunch:
            (u, v) = e[:2]  # ignore edge data if present
            if u in adj and v in adj[u]:
                del adj[u][v]
                if u != v:  # self loop needs only one entry removed
                    del adj[v][u]

    def has_edge(self, u, v):
        """
        Return True if the edge (u,v) is in the graph.
        """

        try:
            return v in self.adj[u]
        except KeyError:
            return False

    def neighbors(self, n):
        """
        Return a list of the nodes connected to the node n.
        """

        try:
            return list(self.adj[n])
        except KeyError:
            raise NetworkXError('The node %s is not in the graph.'
                                % (n, ))

    def neighbors_iter(self, n):
        """
        Return an iterator over all neighbors of node n.
        """

        try:
            return iter(self.adj[n])
        except KeyError:
            raise NetworkXError('The node %s is not in the graph.'
                                % (n, ))

    def edges(self, nbunch=None, data=False):
        return list(self.edges_iter(nbunch, data))

    def edges_iter(self, nbunch=None, data=False):
        """
        Return an iterator over the edges.
        """

        seen = {}  # helper dict to keep track of multiply stored edges
        if nbunch is None:
            nodes_nbrs = self.adj.items()
        else:
            nodes_nbrs = ((n, self.adj[n]) for n in
                self.nbunch_iter(nbunch))
        if data:
            for (n, nbrs) in nodes_nbrs:
                for (nbr, data) in nbrs.items():
                    if nbr not in seen:
                        yield (n, nbr, data)
                seen[n] = 1
        else:
            for (n, nbrs) in nodes_nbrs:
                for nbr in nbrs:
                    if nbr not in seen:
                        yield (n, nbr)
                seen[n] = 1
        del seen

    def get_edge_data(self, u, v, default=None):
        """
        Return the attribute dictionary associated with edge (u,v).
        """

        try:
            return self.adj[u][v]
        except KeyError:
            return default

    def adjacency_list(self):
        """
        Return an adjacency list representation of the graph.
        """

        return list(map(list, iter(self.adj.values())))

    def adjacency_iter(self):
        """
        Return an iterator of (node, adjacency dict) tuples for all nodes.
        """

        return iter(self.adj.items())

    def degree(self, nbunch=None, weight=None):
        """
        Return the degree of a node or nodes.
        """

        if nbunch in self:  # return a single node
            return next(self.degree_iter(nbunch, weight))[1]
        else:

                        # return a dict

            return dict(self.degree_iter(nbunch, weight))

    def degree_iter(self, nbunch=None, weight=None):
        """
        Return an iterator for (node, degree).
        """

        if nbunch is None:
            nodes_nbrs = self.adj.items()
        else:
            nodes_nbrs = ((n, self.adj[n]) for n in
                self.nbunch_iter(nbunch))

        if weight is None:
            for (n, nbrs) in nodes_nbrs:
                yield (n, len(nbrs) + (n in nbrs))  # return tuple (n,degree)
        else:

        # edge weighted graph - degree is sum of nbr edge weights

            for (n, nbrs) in nodes_nbrs:
                yield (n, sum(nbrs[nbr].get(weight, 1) for nbr in nbrs)
                       + (n in nbrs and nbrs[n].get(weight, 1)))

    def clear(self):
        """
        Remove all nodes and edges from the graph.
        """

        self.name = ''
        self.adj.clear()
        self.node.clear()
        self.graph.clear()

    def copy(self):
        """
        Return a copy of the graph.
        """

        return deepcopy(self)

    def is_multigraph(self):
        """Return True if graph is a multigraph, False otherwise."""

        return False

    def is_directed(self):
        """Return True if graph is directed, False otherwise."""

        return False

    def to_directed(self):
        """Return a directed representation of the graph.
        """

        from networkx import DiGraph
        G = DiGraph()
        G.name = self.name
        G.add_nodes_from(self)
        G.add_edges_from((u, v, deepcopy(data)) for (u, nbrs) in
                         self.adjacency_iter() for (v, data) in
                         nbrs.items())
        G.graph = deepcopy(self.graph)
        G.node = deepcopy(self.node)
        return G

    def to_undirected(self):
        """Return an undirected copy of the graph.
        """

        return deepcopy(self)

    def subgraph(self, nbunch):
        """Return the subgraph induced on nodes in nbunch.
        """

        bunch = self.nbunch_iter(nbunch)

        # create new graph and copy subgraph into it

        H = self.__class__()

        # copy node and attribute dictionaries

        for n in bunch:
            H.node[n] = self.node[n]

        # namespace shortcuts for speed

        H_adj = H.adj
        self_adj = self.adj

        # add nodes and edges (undirected method)

        for n in H.node:
            Hnbrs = {}
            H_adj[n] = Hnbrs
            for (nbr, d) in self_adj[n].items():
                if nbr in H_adj:

                    # add both representations of edge: n-nbr and nbr-n

                    Hnbrs[nbr] = d
                    H_adj[nbr][n] = d
        H.graph = self.graph
        return H

    def nodes_with_selfloops(self):
        """Return a list of nodes with self loops.
        """

        return [n for (n, nbrs) in self.adj.items() if n in nbrs]

    def selfloop_edges(self, data=False):
        """Return a list of selfloop edges.
        """

        if data:
            return [(n, n, nbrs[n]) for (n, nbrs) in self.adj.items()
                    if n in nbrs]
        else:
            return [(n, n) for (n, nbrs) in self.adj.items() if n
                    in nbrs]

    def number_of_selfloops(self):
        """Return the number of selfloop edges.
        """

        return len(self.selfloop_edges())

    def size(self, weight=None):
        """Return the number of edges.
        """

        s = sum(self.degree(weight=weight).values()) / 2
        if weight is None:
            return int(s)
        else:
            return float(s)

    def number_of_edges(self, u=None, v=None):
        """Return the number of edges between two nodes.
        """

        if u is None:
            return int(self.size())
        if v in self.adj[u]:
            return 1
        else:
            return 0

    def add_star(self, nodes, **attr):
        """Add a star.
        """

        nlist = list(nodes)
        v = nlist[0]
        edges = ((v, n) for n in nlist[1:])
        self.add_edges_from(edges, **attr)

    def add_path(self, nodes, **attr):
        """Add a path.
        """

        nlist = list(nodes)
        edges = zip(nlist[:-1], nlist[1:])
        self.add_edges_from(edges, **attr)

    def add_cycle(self, nodes, **attr):
        """Add a cycle.
        """

        nlist = list(nodes)
        edges = zip(nlist, nlist[1:] + [nlist[0]])
        self.add_edges_from(edges, **attr)

    def nbunch_iter(self, nbunch=None):
        """Return an iterator of nodes contained in nbunch that are
        """

        if nbunch is None:  # include all nodes via iterator
            bunch = iter(self.adj.keys())
        elif nbunch in self:

                             # if nbunch is a single node

            bunch = iter([nbunch])
        else:

                             # if nbunch is a sequence of nodes

            def bunch_iter(nlist, adj):
                try:
                    for n in nlist:
                        if n in adj:
                            yield n
                except TypeError, e:
                    message = e.args[0]
                    import sys
                    sys.stdout.write(message)

                    # capture error for non-sequence/iterator nbunch.

                    if 'iter' in message:
                        raise NetworkXError('nbunch is not a node or a sequence of nodes.'
                                )
                    elif 'hashable' in message:

                    # capture error for unhashable node.

                        raise NetworkXError('Node %s in the sequence nbunch is not a valid node.'
                                 % n)
                    else:
                        raise

            bunch = bunch_iter(nbunch, self.adj)
        return bunch


#    Copyright (C) 2004-2011 by
#    Aric Hagberg <hagberg@lanl.gov>
#    Dan Schult <dschult@colgate.edu>
#    Pieter Swart <swart@lanl.gov>
#    All rights reserved.
#    BSD license.

from copy import deepcopy


class DiGraph(Graph):

    def __init__(self):

        Graph.__init__(self)
        """
        Initialize a graph with edges, name, graph attributes.
        """

        self.graph = {}  # dictionary for graph attributes
        self.node = {}  # dictionary for node attributes
        # We store two adjacency lists:
        # the  predecessors of node n are stored in the dict self.pred
        # the successors of node n are stored in the dict self.succ=self.adj

        self.adj = {}  # empty adjacency dictionary
        self.pred = {}  # predecessor
        self.succ = self.adj  # successor
        self.edge = self.adj

    def add_node(self, n, attr_dict=None, **attr):
        """
        Add a single node n and update node attributes.
        """
        # set up attribute dict
        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dictionary.')
        if n not in self.succ:
            self.succ[n] = {}
            self.pred[n] = {}
            self.node[n] = attr_dict
        else:
            # update attr even if node already exists
            self.node[n].update(attr_dict)

    def add_nodes_from(self, nodes, **attr):
        """
        Add multiple nodes.
        """

        for n in nodes:
            try:
                newnode = n not in self.succ
            except TypeError:
                (nn, ndict) = n
                if nn not in self.succ:
                    self.succ[nn] = {}
                    self.pred[nn] = {}
                    newdict = attr.copy()
                    newdict.update(ndict)
                    self.node[nn] = newdict
                else:
                    olddict = self.node[nn]
                    olddict.update(attr)
                    olddict.update(ndict)
                continue
            if newnode:
                self.succ[n] = {}
                self.pred[n] = {}
                self.node[n] = attr.copy()
            else:
                self.node[n].update(attr)

    def remove_node(self, n):
        """
        Remove node n.
        """

        try:
            nbrs = self.succ[n]
            del self.node[n]
        except KeyError:

                         # NetworkXError if n not in self

            raise NetworkXError('The node %s is not in the digraph.'
                                % (n, ))
        for u in nbrs:
            del self.pred[u][n]  # remove all edges n-u in digraph
        del self.succ[n]  # remove node from succ
        for u in self.pred[n]:
            del self.succ[u][n]  # remove all edges n-u in digraph
        del self.pred[n]  # remove node from pred

    def remove_nodes_from(self, nbunch):
        """
        Remove multiple nodes.
        """

        for n in nbunch:
            try:
                succs = self.succ[n]
                del self.node[n]
                for u in succs:
                    del self.pred[u][n]  # remove all edges n-u in digraph
                del self.succ[n]  # now remove node
                for u in self.pred[n]:
                    del self.succ[u][n]  # remove all edges n-u in digraph
                del self.pred[n]  # now remove node
            except KeyError:
                pass  # silent failure on remove

    def add_edge(self, u, v, attr_dict=None, **attr):
        """
        Add an edge between u and v.
        """

        # set up attribute dict

        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dictionary.')

        # add nodes

        if u not in self.succ:
            self.succ[u] = {}
            self.pred[u] = {}
            self.node[u] = {}
        if v not in self.succ:
            self.succ[v] = {}
            self.pred[v] = {}
            self.node[v] = {}

        # add the edge

        datadict = self.adj[u].get(v, {})
        datadict.update(attr_dict)
        self.succ[u][v] = datadict
        self.pred[v][u] = datadict

    def add_edges_from(
        self,
        ebunch,
        attr_dict=None,
        **attr
        ):
        """Add all the edges in ebunch.
        """

        # set up attribute dict

        if attr_dict is None:
            attr_dict = attr
        else:
            try:
                attr_dict.update(attr)
            except AttributeError:
                raise NetworkXError('The attr_dict argument must be a dict.'
                                    )

        # process ebunch

        for e in ebunch:
            ne = len(e)
            if ne == 3:
                (u, v, dd) = e
                assert hasattr(dd, 'update')
            elif ne == 2:
                (u, v) = e
                dd = {}
            else:
                raise NetworkXError('Edge tuple %s must be a 2-tuple or 3-tuple.'
                                     % (e, ))
            if u not in self.succ:
                self.succ[u] = {}
                self.pred[u] = {}
                self.node[u] = {}
            if v not in self.succ:
                self.succ[v] = {}
                self.pred[v] = {}
                self.node[v] = {}
            datadict = self.adj[u].get(v, {})
            datadict.update(attr_dict)
            datadict.update(dd)
            self.succ[u][v] = datadict
            self.pred[v][u] = datadict

    def remove_edge(self, u, v):
        """Remove the edge between u and v.
        """

        try:
            del self.succ[u][v]
            del self.pred[v][u]
        except KeyError:
            raise NetworkXError('The edge %s-%s not in graph.' % (u, v))

    def remove_edges_from(self, ebunch):
        """Remove all edges specified in ebunch.
        """

        for e in ebunch:
            (u, v) = e[:2]  # ignore edge data
            if u in self.succ and v in self.succ[u]:
                del self.succ[u][v]
                del self.pred[v][u]

    def has_successor(self, u, v):
        """Return True if node u has successor v.

        This is true if graph has the edge u->v.
        """

        return u in self.succ and v in self.succ[u]

    def has_predecessor(self, u, v):
        """Return True if node u has predecessor v.

        This is true if graph has the edge u<-v.
        """

        return u in self.pred and v in self.pred[u]

    def successors_iter(self, n):
        """Return an iterator over successor nodes of n.

        neighbors_iter() and successors_iter() are the same.
        """

        try:
            return iter(self.succ[n])
        except KeyError:
            raise NetworkXError('The node %s is not in the digraph.'
                                % (n, ))

    def predecessors_iter(self, n):
        """Return an iterator over predecessor nodes of n."""

        try:
            return iter(self.pred[n])
        except KeyError:
            raise NetworkXError('The node %s is not in the digraph.'
                                % (n, ))

    def successors(self, n):
        """Return a list of successor nodes of n.

        neighbors() and successors() are the same function.
        """

        return list(self.successors_iter(n))

    def predecessors(self, n):
        """Return a list of predecessor nodes of n."""

        return list(self.predecessors_iter(n))

    # digraph definitions

    neighbors = successors
    neighbors_iter = successors_iter

    def edges_iter(self, nbunch=None, data=False):
        """Return an iterator over the edges.
        """

        if nbunch is None:
            nodes_nbrs = self.adj.items()
        else:
            nodes_nbrs = ((n, self.adj[n]) for n in
                self.nbunch_iter(nbunch))
        if data:
            for (n, nbrs) in nodes_nbrs:
                for (nbr, data) in nbrs.items():
                    yield (n, nbr, data)
        else:
            for (n, nbrs) in nodes_nbrs:
                for nbr in nbrs:
                    yield (n, nbr)

    # alias out_edges to edges

    out_edges_iter = edges_iter
    out_edges = Graph.edges

    def in_edges_iter(self, nbunch=None, data=False):
        """Return an iterator over the incoming edges.
        """

        if nbunch is None:
            nodes_nbrs = self.pred.items()
        else:
            nodes_nbrs = ((n, self.pred[n]) for n in
                self.nbunch_iter(nbunch))
        if data:
            for (n, nbrs) in nodes_nbrs:
                for (nbr, data) in nbrs.items():
                    yield (nbr, n, data)
        else:
            for (n, nbrs) in nodes_nbrs:
                for nbr in nbrs:
                    yield (nbr, n)

    def in_edges(self, nbunch=None, data=False):
        """Return a list of the incoming edges.

        See Also
        --------
        edges : return a list of edges
        """

        return list(self.in_edges_iter(nbunch, data))

    def degree_iter(self, nbunch=None, weight=None):
        """Return an iterator for (node, degree).
        """

        if nbunch is None:
            nodes_nbrs = zip(iter(self.succ.items()),
                             iter(self.pred.items()))
        else:
            nodes_nbrs = zip(((n, self.succ[n]) for n in
                             self.nbunch_iter(nbunch)), ((n,
                             self.pred[n]) for n in
                             self.nbunch_iter(nbunch)))

        if weight is None:
            for ((n, succ), (n2, pred)) in nodes_nbrs:
                yield (n, len(succ) + len(pred))
        else:

        # edge weighted graph - degree is sum of edge weights

            for ((n, succ), (n2, pred)) in nodes_nbrs:
                yield (n, sum(succ[nbr].get(weight, 1) for nbr in succ)
                       + sum(pred[nbr].get(weight, 1) for nbr in pred))

    def in_degree_iter(self, nbunch=None, weight=None):
        """Return an iterator for (node, in-degree).
        """

        if nbunch is None:
            nodes_nbrs = self.pred.items()
        else:
            nodes_nbrs = ((n, self.pred[n]) for n in
                self.nbunch_iter(nbunch))

        if weight is None:
            for (n, nbrs) in nodes_nbrs:
                yield (n, len(nbrs))
        else:

        # edge weighted graph - degree is sum of edge weights

            for (n, nbrs) in nodes_nbrs:
                yield (n, sum(data.get(weight, 1) for data in
                       nbrs.values()))

    def out_degree_iter(self, nbunch=None, weight=None):
        """Return an iterator for (node, out-degree).
        """

        if nbunch is None:
            nodes_nbrs = self.succ.items()
        else:
            nodes_nbrs = ((n, self.succ[n]) for n in
                self.nbunch_iter(nbunch))

        if weight is None:
            for (n, nbrs) in nodes_nbrs:
                yield (n, len(nbrs))
        else:

        # edge weighted graph - degree is sum of edge weights

            for (n, nbrs) in nodes_nbrs:
                yield (n, sum(data.get(weight, 1) for data in
                       nbrs.values()))

    def in_degree(self, nbunch=None, weight=None):
        """Return the in-degree of a node or nodes.
        """

        if nbunch in self:  # return a single node
            return next(self.in_degree_iter(nbunch, weight))[1]
        else:

                        # return a dict

            return dict(self.in_degree_iter(nbunch, weight))

    def out_degree(self, nbunch=None, weight=None):
        """Return the out-degree of a node or nodes.
        """

        if nbunch in self:  # return a single node
            return next(self.out_degree_iter(nbunch, weight))[1]
        else:

                        # return a dict

            return dict(self.out_degree_iter(nbunch, weight))

    def clear(self):
        """Remove all nodes and edges from the graph.
        """

        self.succ.clear()
        self.pred.clear()
        self.node.clear()
        self.graph.clear()

    def is_multigraph(self):
        """Return True if graph is a multigraph, False otherwise."""

        return False

    def is_directed(self):
        """Return True if graph is directed, False otherwise."""

        return True

    def to_directed(self):
        """Return a directed copy of the graph.
        """

        return deepcopy(self)

    def to_undirected(self, reciprocal=False):
        """Return an undirected representation of the digraph.
        """

        H = Graph()
        H.name = self.name
        H.add_nodes_from(self)
        if reciprocal is True:
            H.add_edges_from((u, v, deepcopy(d)) for (u, nbrs) in
                             self.adjacency_iter() for (v, d) in
                             nbrs.items() if v in self.pred[u])
        else:
            H.add_edges_from((u, v, deepcopy(d)) for (u, nbrs) in
                             self.adjacency_iter() for (v, d) in
                             nbrs.items())
        H.graph = deepcopy(self.graph)
        H.node = deepcopy(self.node)
        return H

    def reverse(self, copy=True):
        """Return the reverse of the graph.
        """

        if copy:
            H = self.__class__(name='Reverse of (%s)' % self.name)
            H.add_nodes_from(self)
            H.add_edges_from((v, u, deepcopy(d)) for (u, v, d) in
                             self.edges(data=True))
            H.graph = deepcopy(self.graph)
            H.node = deepcopy(self.node)
        else:
            (self.pred, self.succ) = (self.succ, self.pred)
            self.adj = self.succ
            H = self
        return H

    def subgraph(self, nbunch):
        """Return the subgraph induced on nodes in nbunch.
        """

        bunch = self.nbunch_iter(nbunch)

        # create new graph and copy subgraph into it

        H = self.__class__()

        # copy node and attribute dictionaries

        for n in bunch:
            H.node[n] = self.node[n]

        # namespace shortcuts for speed

        H_succ = H.succ
        H_pred = H.pred
        self_succ = self.succ

        # add nodes

        for n in H:
            H_succ[n] = {}
            H_pred[n] = {}

        # add edges

        for u in H_succ:
            Hnbrs = H_succ[u]
            for (v, datadict) in self_succ[u].items():
                if v in H_succ:

                    # add both representations of edge: u-v and v-u

                    Hnbrs[v] = datadict
                    H_pred[v][u] = datadict
        H.graph = self.graph
        return H


DEFAULT_RISKS = {
    INTERNET_RISK: ('INTERNET_RISK', (195, 255, 0)),
    PRIVACY_RISK: ('PRIVACY_RISK', (255, 255, 51)),
    PHONE_RISK: ('PHONE_RISK', (255, 216, 0)),
    SMS_RISK: ('SMS_RISK', (255, 93, 0)),
    MONEY_RISK: ('MONEY_RISK', (255, 0, 0)),
    }

DEXCLASSLOADER_COLOR = (0, 0, 0)
ACTIVITY_COLOR = (51, 255, 51)
SERVICE_COLOR = (0, 204, 204)
RECEIVER_COLOR = (204, 51, 204)

ID_ATTRIBUTES = {
    'type': 0,
    'class_name': 1,
    'method_name': 2,
    'descriptor': 3,
    'permissions': 4,
    'permissions_level': 5,
    'dynamic_code': 6,
    }


class CFGAnalysis(object):

    def __init__(self, vmx, apk):  # vmx => NewVmAnalysis
        self.vmx = vmx
        self.vms = vmx.get_vms()
        self.apk = apk

        self.block_number = 0
        self.blocks = {}

        self.nodes = {}         # key => NodeF
        self.nodes_id = {}      # id => NodeF
        self.entry_nodes = []
        self.G = DiGraph()
        self.GI = DiGraph()

    def export_to_dot(self):
        buff = "digraph CFG {\n"
        buff += self.generate_block_points()
        buff += self.generate_block_edges()
        buff += "}"
        return buff

    def generate_block_points(self):
        buff = ""
        for vm in self.vms:
            for method in vm.get_methods():
                g = self.vmx.get_method_novm(vm, method)  # g => MethodAnalysis
                # self.block_number += len(g.basic_blocks.bb)
                for block in g.basic_blocks.get():
                    buff += '"' + block.name + '"' + '\n'
        return buff

    def generate_block_edges(self):
        buff = ""
        for vm in self.vms:
            for method in vm.get_methods():
                g = self.vmx.get_method_novm(vm, method)
                for block in g.basic_blocks.get():
                    for child_block in block.childs:
                        buff += '"' + block.name + '"' + " -> " + '"' + child_block[2].get_name() + '"' + '\n'
        return buff

    def generate_cfg(self, vmx, apk):

        for j in self.vmx.tainted_packages.get_internal_packages():     # j: PathP
            (src_class_name, src_method_name, src_descriptor) = j.get_src(self.vm.get_class_manager())
            (dst_class_name, dst_method_name, dst_descriptor) = j.get_dst(self.vm.get_class_manager())
            if src_class_name.find("Landroid/support/") == -1:
                n1 = self._get_node(src_class_name, src_method_name, src_descriptor)
                n2 = self._get_node(dst_class_name, dst_method_name, dst_descriptor)

                self.G.add_edge(n1.id, n2.id)
                n1.add_edge(n2, j)
                # print >> out_file, src_class_name + "---" + src_method_name + "----" + src_descriptor
                # print >> out_file, dst_class_name + "---" + dst_method_name + "----" + dst_descriptor

        internal_new_packages = self.vmx.tainted_packages.get_internal_new_packages()
        for j in internal_new_packages:
            for path in internal_new_packages[j]:
                (src_class_name, src_method_name, src_descriptor) = path.get_src(self.vm.get_class_manager())
                if src_class_name.find("Landroid/support/") == -1:
                    # print >> out_file, src_class_name + "----" + src_method_name + "----" + src_descriptor
                    n1 = self._get_node(src_class_name, src_method_name, src_descriptor)
                    n2 = self._get_node(j, '', '')
                    self.GI.add_edge(n2.id, n1.id)
                    n1.add_edge(n2, path)

        # out_file.close()

        # link the component to its life cycle and life cycle callbacks
        self.link_activities(apk)
        self.link_services(apk)
        self.link_receivers(apk)



        # Specific Java/Android library callbacks
        self.link_callbacks()

            # elif c.get_superclassname() == "Landroid/os/AsyncTask;":
            #    for i in self.vm.get_method("doInBackground"):
            #        if i.get_class_name() == c.get_name():
            #            n1 = self._get_node( i.get_class_name(), i.get_name(), i.get_descriptor() )
            #            n2 = self._get_exist_node( i.get_class_name(), "execute", i.get_descriptor() )
            #            print n1, n2, i.get_descriptor()
                        # for j in self.vm.get_method("doInBackground"):
                        #    n2 = self._get_exist_node( i.get_class_name(), j.get_name(), j.get_descriptor() )
                        #    print n1, n2
                        # n2 = self._get_node( i.get_class_name(), "
            #    raise("ooo")

        # for j in self.vmx.tainted_packages.get_internal_new_packages():
        #    print "\t %s %s %s %x ---> %s %s %s" % (j.get_method().get_class_name(), j.get_method().get_name(), j.get_method().get_descriptor(), \
        #                                            j.get_bb().start + j.get_idx(), \
        #                                            j.get_class_name(), j.get_name(), j.get_descriptor())

        list_permissions = self.vmx.get_permissions([])
        for x in list_permissions:
            for j in list_permissions[x]:
                if isinstance(j, PathVar):
                    continue

                (src_class_name, src_method_name, src_descriptor) = \
                    j.get_src(self.vm.get_class_manager())
                (dst_class_name, dst_method_name, dst_descriptor) = \
                    j.get_dst(self.vm.get_class_manager())
                n1 = self._get_exist_node(dst_class_name,
                        dst_method_name, dst_descriptor)

                if n1 is None:
                    continue

                n1.set_attributes({'permissions': 1})
                n1.set_attributes({'permissions_level': DVM_PERMISSIONS['MANIFEST_PERMISSION'
                                  ][x][0]})
                n1.set_attributes({'permissions_details': x})

                try:
                    for tmp_perm in PERMISSIONS_RISK[x]:
                        if tmp_perm in DEFAULT_RISKS:
                            n2 = self._get_new_node(dst_class_name,
                                    dst_method_name, dst_descriptor
                                    + ' ' + DEFAULT_RISKS[tmp_perm][0],
                                    DEFAULT_RISKS[tmp_perm][0])
                            n2.set_attributes({'color': DEFAULT_RISKS[tmp_perm][1]})
                            self.G.add_edge(n2.id, n1.id)

                            n1.add_risk(DEFAULT_RISKS[tmp_perm][0])
                            n1.add_api(x, src_class_name + '-'
                                    + src_method_name + '-'
                                    + src_descriptor)
                except KeyError:
                    pass

        # Tag DexClassLoader

        for (m, _) in self.vmx.get_tainted_packages().get_packages():
            if m.get_name() == 'Ldalvik/system/DexClassLoader;':
                for path in m.get_paths():
                    if path.get_access_flag() == TAINTED_PACKAGE_CREATE:
                        (src_class_name, src_method_name,
                         src_descriptor) = \
                            path.get_src(self.vm.get_class_manager())
                        n1 = self._get_exist_node(src_class_name,
                                src_method_name, src_descriptor)
                        n2 = self._get_new_node(dst_class_name,
                                dst_method_name, dst_descriptor + ' '
                                + 'DEXCLASSLOADER', 'DEXCLASSLOADER')

                        n1.set_attributes({'dynamic_code': 'true'})
                        n2.set_attributes({'color': DEXCLASSLOADER_COLOR})
                        self.G.add_edge(n2.id, n1.id)

                        n1.add_risk('DEXCLASSLOADER')

    def link_callbacks(self):
        for c in self.vm.get_classes():

            # if c.get_superclassname() == "Landroid/app/Service;":
            #    n1 = self._get_node( c.get_name(), "<init>", "()V" )
            #    n2 = self._get_node( c.get_name(), "onCreate", "()V" )

            #    self.G.add_edge( n1.id, n2.id )
            # for method in c.get_methods():



            if c.get_superclassname() == 'Ljava/lang/Thread;' \
                or c.get_superclassname() == 'Ljava/util/TimerTask;':
                for i in self.vm.get_method_novm('run'):
                    if i.get_class_name() == c.get_name():
                        n1 = self._get_node(i.get_class_name(),
                                i.get_name(), i.get_descriptor())
                        n2 = self._get_node(i.get_class_name(), 'start'
                                , i.get_descriptor())

                        # link from start to run

                        self.G.add_edge(n2.id, n1.id)
                        n2.add_edge(n1, {})

                        # link from init to start

                        for init in self.vm.get_method_novm('<init>'):
                            if init.get_class_name() == c.get_name():
                                n3 = \
                                    self._get_node(init.get_class_name(),
                                        '<init>', init.get_descriptor())

                                # n3 = self._get_node( i.get_class_name(), "<init>", i.get_descriptor() )

                                self.G.add_edge(n3.id, n2.id)
                                n3.add_edge(n2, {})

    def link_receivers(self, apk):
        if apk is not None:
            for i in apk.get_receivers():       # link Receiver to onReceive
                    j = bytecode.FormatClassToJava(i)
                    n1 = self._get_exist_node(j, 'onReceive',
                            '(Landroid/content/Context; Landroid/content/Intent;)V'
                            )
                    if n1 is not None:
                        n1.set_attributes({'type': 'receiver'})
                        n1.set_attributes({'color': RECEIVER_COLOR})
                        n2 = self._get_new_node_from(n1, 'RECEIVER' + i.split('.')[-1])
                        n2.set_attributes({'color': RECEIVER_COLOR})
                        self.G.add_edge(n2.id, n1.id)
                        self.entry_nodes.append(n1.id)

    def link_services(self, apk):
        if apk is not None:
            for i in apk.get_services():        # link Service to onCreate
                j = bytecode.FormatClassToJava(i)
                n1 = self._get_exist_node(j, 'onCreate', '()V')

                if n1 is not None:
                    n1.set_attributes({'type': 'service'})
                    n1.set_attributes({'color': SERVICE_COLOR})
                    n2 = self._get_new_node_from(n1, 'SERVICE' + i.split('.')[-1] )
                    n2.set_attributes({'color': SERVICE_COLOR})
                    self.G.add_edge(n2.id, n1.id)
                    self.entry_nodes.append(n1.id)
                    n3 = self._get_exist_node(j, 'onStartCommand', '(Landroid/content/Intent; I; I;)I')

                    n4 = self._get_exist_node(j, "onBind", '(Landroid/content/Intent;)Landroid/os/IBinder')

                    branch = self._get_new_node(j, 'branch', 'In the center of Service', '')
                    n5 = self._get_exist_node(j, 'onUnbind', '(Landroid/content/Intent)V')
                    n6 = self._get_exist_node(j, "onDestroy", '()V')


                    if n3 is not None or n4 is not None:
                        if n3 is not None:
                            self.G.add_edge(n1.id, n3.id)
                            self.G.add_edge(n3.id, branch.id)
                        if n4 is not None:
                            self.G.add_edge(n1.id, n4.id)
                            self.G.add_edge(n4.id, branch.id)
                    else:
                        self.G.add_edge(n1.id, branch.id)

                    if n5 is not None:
                        self.G.add_edge(branch.id, n5.id)
                        if n6 is not None:
                            self.G.add_edge(n5.id, n6.id)
                    else:
                        if n6 is not None:
                            self.G.add_edge(branch.id, n6.id)

    def link_activities(self, apk):
        if apk is not None:
            for i in apk.get_activities():      # link Activity to onCreate
                j = bytecode.FormatClassToJava(i)

                n1 = self._get_exist_node(j, 'onCreate', '(Landroid/os/Bundle;)V')  # n1: NodeF
                if n1 is not None:
                    n1.set_attributes({'type': 'activity'})
                    n1.set_attributes({'color': ACTIVITY_COLOR})
                    n2 = self._get_new_node_from(n1, 'ACTIVITY' + i.split('.')[-1])
                    n2.set_attributes({'color': ACTIVITY_COLOR})
                    self.G.add_edge(n2.id, n1.id)
                    self.entry_nodes.append(n1.id)

                    n2 = self._get_exist_node(j, 'onStart', '()V')
                    if n2 is not None:
                        self.G.add_edge(n1.id, n2.id)       #link onCreate ot onStart
                        n3 = self._get_exist_node(j, 'onResume', '()V')
                        if n3 is not None:
                            self.G.add_edge(n2.id, n3.id)       # link onStart to onResume
                            branch = self._get_new_node(j, 'branch', "In the center of Activity", '')
                            self.G.add_edge(n3.id, branch.id)   # link onResume to branch
                    else:
                        n3 = self._get_exist_node(j, 'onResume', '()V')
                        if n3 is not None:
                            self.G.add_edge(n1.id, n3.id)   # link onCreate to onResume
                            branch = self._get_new_node(j, 'branch', "In the center of Activity", 'no')
                            self.G.add_edge(n3.id, branch.id)   # link onResume to branch
                        else:
                            branch = self._get_new_node(j, 'branch', "In the center of Activity", 'no')
                            self.G.add_edge(n1.id, branch.id)   #link onCrate to branch

                branch = self._get_exist_node(j, "branch", "In the center of Activity")
                if branch is not None:
                    n4 = self._get_exist_node(j, 'onPause', '()V')
                    n5 = self._get_exist_node(j, 'onStop', '()V')
                    n6 = self._get_exist_node(j, 'onDestroy', '()V')
                    if n4 is not None:
                        self.G.add_edge(branch.id, n4.id)
                        if n5 is not None:
                            self.G.add_edge(n4.id, n5.id)
                            if n6 is not None:
                                self.G.add_edge(n5.id, n6.id)
                        else:
                            if n6 is not None:
                                self.G.add_edge(n4.id, n6.id)
                    else:
                        if n5 is not None:
                            self.G.add_edge(branch.id, n5.id)
                            if n6 is not None:
                                self.G.add_edge(n5.id, n6.id)
                        else:
                            if n6 is not None:
                                self.G.add_edge(branch.id, n6.id)

    def _get_exist_node(self, class_name, method_name, descriptor):
        key = '%s %s %s' % (class_name, method_name, descriptor)
        try:
            return self.nodes[key]
        except KeyError:
            return None

    def _get_node(self, class_name, method_name, descriptor):
        if method_name == '' and descriptor == '':
            key = class_name
        else:
            key = '%s %s %s' % (class_name, method_name, descriptor)
        if key not in self.nodes:
            self.nodes[key] = NodeF(len(self.nodes), class_name, method_name, descriptor)
            self.nodes_id[self.nodes[key].id] = self.nodes[key]
        return self.nodes[key]

    def _get_new_node_from(self, n, label):
        return self._get_new_node(n.class_name, n.method_name, n.descriptor + label, label)

    def _get_new_node(self, class_name, method_name, descriptor, label):
        key = '%s %s %s' % (class_name, method_name, descriptor)
        if key not in self.nodes:
            self.nodes[key] = NodeF( len(self.nodes), class_name, method_name, descriptor, label, False)
            self.nodes_id[self.nodes[key].id] = self.nodes[key]

        return self.nodes[key]

    def set_new_attributes(self, cm):
        for i in self.G.nodes():
            n1 = self.nodes_id[i]
            m1 = self.vm.get_method_descriptor(n1.class_name,
                    n1.method_name, n1.descriptor)

            H = cm(self.vmx, m1)

            n1.set_attributes(H)

    def export_to_gexf(self):
        buff = '<?xml version="1.0" encoding="UTF-8"?>\n'
        buff += \
            '<gexf xmlns="http://www.gephi.org/gexf" xmlns:viz="http://www.gephi.org/gexf/viz">\n'
        buff += '<graph type="static">\n'

        buff += '<attributes class="node" type="static">\n'
        buff += \
            '<attribute default="normal" id="%d" title="type" type="string"/>\n' \
            % ID_ATTRIBUTES['type']
        buff += \
            '<attribute id="%d" title="class_name" type="string"/>\n' \
            % ID_ATTRIBUTES['class_name']
        buff += \
            '<attribute id="%d" title="method_name" type="string"/>\n' \
            % ID_ATTRIBUTES['method_name']
        buff += \
            '<attribute id="%d" title="descriptor" type="string"/>\n' \
            % ID_ATTRIBUTES['descriptor']

        buff += \
            '<attribute default="0" id="%d" title="permissions" type="integer"/>\n' \
            % ID_ATTRIBUTES['permissions']
        buff += \
            '<attribute default="normal" id="%d" title="permissions_level" type="string"/>\n' \
            % ID_ATTRIBUTES['permissions_level']

        buff += \
            '<attribute default="false" id="%d" title="dynamic_code" type="boolean"/>\n' \
            % ID_ATTRIBUTES['dynamic_code']
        buff += '</attributes>\n'

        buff += '<nodes>\n'
        for node in self.G.nodes():
            buff += '<node id="%d" label="%s">\n' % (node,
                    escape(self.nodes_id[node].label))
            buff += self.nodes_id[node].get_attributes_gexf()
            buff += '</node>\n'
        buff += '</nodes>\n'

        buff += '<edges>\n'
        nb = 0
        for edge in self.G.edges():
            buff += '<edge id="%d" source="%d" target="%d"/>\n' % (nb,
                    edge[0], edge[1])
            nb += 1
        buff += '</edges>\n'

        buff += '</graph>\n'
        buff += '</gexf>\n'

        return buff

    def export_to_gml(self):
        buff = \
            '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n'
        buff += \
            '<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">\n'

        buff += \
            '<key attr.name="description" attr.type="string" for="node" id="d5"/>\n'
        buff += '<key for="node" id="d6" yfiles.type="nodegraphics"/>\n'

        buff += '<graph edgedefault="directed" id="G">\n'

        for node in self.G.nodes():
            buff += '<node id="%d">\n' % node

            # fd.write( "<node id=\"%d\" label=\"%s\">\n" % (node, escape(self.nodes_id[ node ].label)) )

            buff += self.nodes_id[node].get_attributes_gml()
            buff += '</node>\n'

        nb = 0
        for edge in self.G.edges():
            buff += '<edge id="%d" source="%d" target="%d"/>\n' % (nb,
                    edge[0], edge[1])
            nb += 1

        buff += '</graph>\n'
        buff += '</graphml>\n'

        return buff


DEFAULT_NODE_TYPE = 'normal'
DEFAULT_NODE_PERM = 0
DEFAULT_NODE_PERM_LEVEL = -1

PERMISSIONS_LEVEL = {
    'dangerous': 3,
    'signatureOrSystem': 2,
    'signature': 1,
    'normal': 0,
    }

COLOR_PERMISSIONS_LEVEL = {
    'dangerous': (255, 0, 0),
    'signatureOrSystem': (255, 63, 63),
    'signature': (255, 132, 132),
    'normal': (255, 181, 181),
    }


class NodeF(object):

    def __init__(self, ids, class_name, method_name, descriptor, label=None, real=True,):
        self.class_name = class_name
        self.method_name = method_name
        self.descriptor = descriptor

        self.id = ids
        self.real = real
        self.risks = []
        self.api = {}
        self.edges = {}

        if label is None:
            self.label = '%s %s %s' % (class_name, method_name,
                    descriptor)
        else:
            self.label = label

        self.attributes = {
            'type': DEFAULT_NODE_TYPE,
            'color': None,
            'permissions': DEFAULT_NODE_PERM,
            'permissions_level': DEFAULT_NODE_PERM_LEVEL,
            'permissions_details': set(),
            'dynamic_code': 'false',
            }

    def add_edge(self, n, idx):
        try:
            self.edges[n].append(idx)
        except KeyError:
            self.edges[n] = []
            self.edges[n].append(idx)

    def get_attributes_gexf(self):
        buff = ''

        if self.attributes['color'] is not None:
            buff += '<viz:color r="%d" g="%d" b="%d"/>\n' \
                % (self.attributes['color'][0], self.attributes['color'
                   ][1], self.attributes['color'][2])

        buff += '<attvalues>\n'
        buff += '<attvalue id="%d" value="%s"/>\n' \
            % (ID_ATTRIBUTES['class_name'], escape(self.class_name))
        buff += '<attvalue id="%d" value="%s"/>\n' \
            % (ID_ATTRIBUTES['method_name'], escape(self.method_name))
        buff += '<attvalue id="%d" value="%s"/>\n' \
            % (ID_ATTRIBUTES['descriptor'], escape(self.descriptor))

        if self.attributes['type'] != DEFAULT_NODE_TYPE:
            buff += '<attvalue id="%d" value="%s"/>\n' \
                % (ID_ATTRIBUTES['type'], self.attributes['type'])
        if self.attributes['permissions'] != DEFAULT_NODE_PERM:
            buff += '<attvalue id="%d" value="%s"/>\n' \
                % (ID_ATTRIBUTES['permissions'],
                   self.attributes['permissions'])
            buff += '<attvalue id="%d" value="%s"/>\n' \
                % (ID_ATTRIBUTES['permissions_level'],
                   self.attributes['permissions_level_name'])

        buff += '<attvalue id="%d" value="%s"/>\n' \
            % (ID_ATTRIBUTES['dynamic_code'],
               self.attributes['dynamic_code'])

        buff += '</attvalues>\n'

        return buff

    def get_attributes_gml(self):
        buff = ''

        buff += '<data key="d6">\n'
        buff += '<y:ShapeNode>\n'

        height = 10
        width = max(len(self.class_name), len(self.method_name))
        width = max(width, len(self.descriptor))

        buff += '<y:Geometry height="%f" width="%f"/>\n' % (16
                * height, 8 * width)
        if self.attributes['color'] is not None:
            buff += \
                '<y:Fill color="#%02x%02x%02x" transparent="false"/>\n' \
                % (self.attributes['color'][0], self.attributes['color'
                   ][1], self.attributes['color'][2])

        buff += \
            '<y:NodeLabel alignment="left" autoSizePolicy="content" fontFamily="Dialog" fontSize="13" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" modelName="internal" modelPosition="c" textColor="#000000" visible="true">\n'

        label = self.class_name + """\n""" + self.method_name \
            + """\n""" + self.descriptor
        buff += escape(label)

        buff += '</y:NodeLabel>\n'
        buff += '</y:ShapeNode>\n'
        buff += '</data>\n'

        return buff

    def get_attributes(self):
        return self.attributes

    def get_attribute(self, name):
        return self.attributes[name]

    def set_attributes(self, values):
        for i in values:
            if i == 'permissions':
                self.attributes['permissions'] += values[i]
            elif i == 'permissions_level':
                if values[i] > self.attributes['permissions_level']:
                    self.attributes['permissions_level'] = \
                        PERMISSIONS_LEVEL[values[i]]
                    self.attributes['permissions_level_name'] = \
                        values[i]
                    self.attributes['color'] = \
                        COLOR_PERMISSIONS_LEVEL[values[i]]
            elif i == 'permissions_details':
                self.attributes[i].add(values[i])
            else:
                self.attributes[i] = values[i]

    def add_risk(self, risk):
        if risk not in self.risks:
            self.risks.append(risk)

    def add_api(self, perm, api):
        if perm not in self.api:
            self.api[perm] = []

        if api not in self.api[perm]:
            self.api[perm].append(api)

