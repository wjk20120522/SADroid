#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of Androguard.
#
# Copyright (C) 2012, Anthony Desnos <desnos at t0t0.fr>
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# frameworks/base/core/res/AndroidManifest.xml
########################################## PERMISSIONS ########################################################

DVM_PERMISSIONS = {'MANIFEST_PERMISSION': {  # COST_MONEY  (new added)
                                             # MESSAGES
                                             # SOCIAL_INFO
                                             # PERSONAL_INFO
                                             # CALENDAR
                                             # USER_DICTIONARY
                                             # WRITE_USER_DICTIONARY
                                             # BOOKMARKS
                                             # DEVICE_ALARMS
                                             # VOICEMAIL
                                             # ACCESSIBILITY_FEATURES (new added)
                                             # LOCATION
                                             # NETWORK
                                             # BLUETOOTH_NETWORK
                                             # ACCOUNTS
                                             # AFFECTS_BATTERY
                                             # AUDIO_SETTINGS
                                             # HARDWARE_CONTROLS
                                             # MICROPHONE
                                             # CAMERA
                                             # PHONE_CALLS
                                             # STORAGE
                                             # SCREENLOCK
                                             # APP_INFO
                                             # DISPLAY
                                             # WALLPAPER
                                             # SYSTEM_CLOCK
                                             # STATUS_BAR
                                             # SYNC_SETTINGS
                                             # SYSTEM TOOLS
                                             # DEVELOPMENT_TOOLS
                                             # No groups ...
    'android.permission.SEND_SMS': ['dangerous', 'send SMS messages',
                 'Allows application to send SMS messages. Malicious applications may cost you money by sending messages without your confirmation.'
                 ],
    'android.permission.SEND_RESPOND_VIA_MESSAGE': ['signatureOrSystem', 'send respond-via-message events',
                                 'Allows the app to send requests to other messaging apps to handle respond-via-message events for incoming calls.'],
    'android.permission.RECEIVE_SMS': ['dangerous', 'receive SMS',
                    'Allows application to receive and process SMS messages. Malicious applications may monitor your messages or delete them without showing them to you.'
                    ],
    'android.permission.RECEIVE_MMS': ['dangerous', 'receive MMS',
                    'Allows application to receive and process MMS messages. Malicious applications may monitor your messages or delete them without showing them to you.'
                    ],
    'android.permission.CARRIER_FILTER_SMS': ['signatureOrSystem', 'hide', 'Allows an application to filter carrier specific sms'],
    'android.permission.RECEIVE_EMERGENCY_BROADCAST': ['signatureOrSystem', 'hide',
                                    'Allows an application to receive emergency cell broadcast messages, to record or display them to the user. Reserved for system apps.'
                                    ],
    'android.permission.READ_CELL_BROADCASTS': ['dangerous',
                             'received cell broadcast messages',
                             'Allows an application to read previously received cell broadcast messages and to register a content observer to get notifications when a cell broadcast has been received and added to the database. For emergency alerts, the database is updated immediately after the alert dialog and notification sound/vibration/speech are presented.The "read" column is then updated after the user dismisses the alert.This enables supplementary emergency assistance apps to start loading additional emergency information (if Internet access is available) when the alert is first received, and to delay presenting the info to the user until after the initial alert dialog is dismissed.'
                             ],
    'android.permission.READ_SMS': ['dangerous', 'read SMS or MMS',
                 'Allows application to read SMS messages stored on your phone or SIM card. Malicious applications may read your confidential messages.'
                 ],
    'android.permission.WRITE_SMS': ['dangerous', 'edit SMS or MMS',
                  'Allows application to write to SMS messages stored on your phone or SIM card. Malicious applications may delete your messages.'
                  ],
    'android.permission.RECEIVE_WAP_PUSH': ['dangerous', 'receive WAP',
                         'Allows application to receive and process WAP messages. Malicious applications may monitor your messages or delete them without showing them to you.'
                         ],
    'android.permission.RECEIVE_BLUETOOTH_MAP': ['signatureOrSystem', 'receive Bluetooth messages (MAP)', 'Allows an application to monitor incoming Bluetooth MAP messages, to record or perform processing on them'],
    'android.permission.READ_CONTACTS': ['dangerous', 'read contact data',
                      'Allows an application to read all of the contact (address) data stored on your phone. Malicious applications can use this to send your data to other people.'
                      ],
    'android.permission.WRITE_CONTACTS': ['dangerous', 'write contact data',
                       'Allows an application to modify the contact (address) data stored on your phone. Malicious applications can use this to erase or modify your contact data.'
                       ],
    'android.permission.BIND_DIRECTORY_SEARCH': ['signatureOrSystem',
                              'execute contacts directory search',
                              'Allows an application to execute contacts directory search. This should only be used by ContactsProvider.'
                              ],
    'android.permission.READ_CALL_LOG': ['dangerous', "read the user's call log.",
                      "Allows an application to read the user's call log."
                      ],
    'android.permission.WRITE_CALL_LOG': ['dangerous',
                       "write (but not read) the user's contacts data."
                       ,
                       "Allows an application to write (but not read) the user's contacts data."
                       ],
    'android.permission.READ_SOCIAL_STREAM': ['dangerous',
                           "read from the user's social stream",
                           "Allows an application to read from the user's social stream."
                           ],
    'android.permission.WRITE_SOCIAL_STREAM': ['dangerous',
                            "write the user's social stream",
                            "Allows an application to write (but not read) the user's social stream data."
                            ],
    'android.permission.READ_PROFILE': ['dangerous',
                     "read the user's personal profile data",
                     "Allows an application to read the user's personal profile data."
                     ],
    'android.permission.WRITE_PROFILE': ['dangerous',
                      "write the user's personal profile data",
                      "Allows an application to write (but not read) the user's personal profile data."
                      ],
    'android.permission.BODY_SENSORS':['', 'body sensors (like heart rate monitors)','Allows the app to access data from sensors that monitor your physical condition, such as your heart rate.'],
    'android.permission.READ_CALENDAR': ['dangerous', 'read calendar events',
                      'Allows an application to read all of the calendar events stored on your phone. Malicious applications can use this to send your calendar events to other people.'
                      ],
    'android.permission.WRITE_CALENDAR': ['dangerous',
                       'add or modify calendar events and send emails to guests'
                       ,
                       'Allows an application to add or change the events on your calendar, which may send emails to guests. Malicious applications can use this to erase or modify your calendar events or to send emails to guests.'
                       ],
    'android.permission.READ_USER_DICTIONARY': ['dangerous', 'read user-defined dictionary'
                             ,
                             'Allows an application to read any private words, names and phrases that the user may have stored in the user dictionary.'
                             ],
    'android.permission.WRITE_USER_DICTIONARY': ['normal',
                              'write to user-defined dictionary',
                              'Allows an application to write new words into the user dictionary.'
                              ],
    'com.android.browser.permission.READ_HISTORY_BOOKMARKS': ['dangerous',
                               "read Browser's history and bookmarks",
                               "Allows the application to read all the URLs that the browser has visited and all of the browser\'s bookmarks."
                               ],
    'com.android.browser.permission.WRITE_HISTORY_BOOKMARKS': ['dangerous',
                                "write Browser's history and bookmarks"
                                ,
                                "Allows an application to modify the browser\'s history or bookmarks stored on your phone. Malicious applications can use this to erase or modify your browser\'s data."
                                ],
    'com.android.alarm.permission.SET_ALARM': ['normal', 'set alarm in alarm clock',
                  'Allows the application to set an alarm in an installed alarm clock application. Some alarm clock applications may not implement this feature.'
                  ],
    'com.android.voicemail.permission.ADD_VOICEMAIL': ['dangerous', 'add voicemails into the system',
                      'Allows an application to add voicemails into the system.'
                      ],
    'com.android.voicemail.permission.WRITE_VOICEMAIL': ['signatureOrSystem', '', 'Allows an application to modify and remove existing voicemails in the system'],
    'com.android.voicemail.permission.READ_VOICEMAIL': ['signatureOrSystem', 'read voicemail', 'Allows the app to read your voicemails.'],
    'android.permission.ACCESS_FINE_LOCATION': ['dangerous', 'fine (GPS) location',
                             'Access fine location sources, such as the Global Positioning System on the phone, where available. Malicious applications can use this to determine where you are and may consume additional battery power.'
                             ],
    'android.permission.ACCESS_COARSE_LOCATION': ['dangerous',
                               'coarse (network-based) location',
                               'Access coarse location sources, such as the mobile network database, to determine an approximate phone location, where available. Malicious applications can use this to determine approximately where you are.'
                               ],
    'android.permission.ACCESS_MOCK_LOCATION': ['dangerous',
                             'mock location sources for testing',
                             'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers.'
                             ],
    'android.permission.ACCESS_LOCATION_EXTRA_COMMANDS': ['normal',
            'access extra location provider commands',
            'Access extra location provider commands. Malicious applications could use this to interfere with the operation of the GPS or other location sources.'
            ],
    'android.permission.INSTALL_LOCATION_PROVIDER': ['signatureOrSystem',
                                  'permission to install a location provider'
                                  ,
                                  'Create mock location sources for testing. Malicious applications can use this to override the location and/or status returned by real-location sources such as GPS or Network providers, or monitor and report your location to an external source.'
                                  ],
    'android.permission.HDMI_CEC': ['signatureOrSystem', 'hide', 'Allows HDMI-CEC service to access device and configuration files.This should only be used by HDMI-CEC service'],
    'android.permission.LOCATION_HARDWARE': ['signatureOrSystem', 'hide', 'Allows an application to use location features in hardware,Allows an application to use location features in hardware'],
    'android.permission.INTERNET': ['dangerous', 'full Internet access',
                 'Allows an application to create network sockets.'],
    'android.permission.ACCESS_NETWORK_STATE': ['normal', 'view network status',
                             'Allows an application to view the status of all networks.'
                             ],
    'android.permission.ACCESS_WIFI_STATE': ['normal', 'view Wi-Fi status',
                          'Allows an application to view the information about the status of Wi-Fi.'
                          ],
    'android.permission.CHANGE_WIFI_STATE': ['dangerous', 'change Wi-Fi status',
                          'Allows an application to connect to and disconnect from Wi-Fi access points and to make changes to configured Wi-Fi networks.'
                          ],
    'android.permission.READ_WIFI_CREDENTIAL': ['signatureOrSystem', 'hide', 'Allows applications to read Wi-Fi credential.'],
    'android.permission.ACCESS_WIMAX_STATE': ['normal', 'connect and disconnect from WiMAX', 'Allows the app to determine whether WiMAX is enabled and information about any WiMAX networks that are connected.'],
    'android.permission.CHANGE_WIMAX_STATE': ['dangerous', 'change WiMAX state', 'Allows the app to connect the phone to and disconnect the phone from WiMAX networks.'],
    'android.permission.SCORE_NETWORKS': ['normal', 'score networks', 'Allows the app to rank networks and influence which networks the phone should prefer.'],
    'android.permission.BLUETOOTH': ['dangerous', 'create Bluetooth connections',
                  'Allows an application to view configuration of the local Bluetooth phone and to make and accept connections with paired devices.'
                  ],
    'android.permission.BLUETOOTH_ADMIN': ['dangerous', 'bluetooth administration',
                        'Allows an application to configure the local Bluetooth phone and to discover and pair with remote devices.'
                        ],
    'android.permission.BLUETOOTH_PRIVILEGED': ['signatureOrSystem', 'allow Bluetooth pairing by Application', 'Allows the app to pair with remote devices without user interaction.'],
    'android.permission.BLUETOOTH_MAP': ['signature', 'access Bluetooth MAP data', 'Allows the app to access Bluetooth MAP data.'],
    'android.permission.BLUETOOTH_STACK': ['signature', 'hide', 'Allows bluetooth stack to access files'],
    'android.permission.NFC': ['dangerous', 'control Near-Field Communication',
            'Allows an application to communicate with Near-Field Communication (NFC) tags, cards and readers.'
            ],
    'android.permission.CONNECTIVITY_INTERNAL': ['signatureOrSystem',
                              'use privileged ConnectivityManager API',
                              'Allows an internal user to use privileged ConnectivityManager API'
                              ],
    'android.permission.RECEIVE_DATA_ACTIVITY_CHANGE': ['signatureOrSystem', '', ''],
    'android.permission.LOOP_RADIO': ['signatureOrSystem', 'hide', 'Allows access to the loop radio (Android mesh network) device'],
    'android.permission.NFC_HANDOVER_STATUS': ['signatureOrSystem', 'Receive Android Beam transfer status', 'Allows this application to receive information about current Android Beam transfers'],
    'android.permission.GET_ACCOUNTS': ['normal', 'discover known accounts',
                     'Allows an application to access the list of accounts known by the phone.'
                     ],
    'android.permission.AUTHENTICATE_ACCOUNTS': ['dangerous',
                              'act as an account authenticator',
                              'Allows an application to use the account authenticator capabilities of the Account Manager, including creating accounts as well as obtaining and setting their passwords.'
                              ],
    'android.permission.USE_CREDENTIALS': ['dangerous',
                        'use the authentication credentials of an account'
                        ,
                        'Allows an application to request authentication tokens.'
                        ],
    'android.permission.MANAGE_ACCOUNTS': ['dangerous', 'manage the accounts list',
                        'Allows an application to perform operations like adding and removing accounts and deleting their password.'
                        ],
    'android.permission.ACCOUNT_MANAGER': ['signature',
                        'act as the Account Manager Service',
                        'Allows an application to make calls to Account Authenticators'
                        ],
    'android.permission.CHANGE_WIFI_MULTICAST_STATE': ['dangerous',
                                    'allow Wi-Fi Multicast reception',
                                    'Allows an application to receive packets not directly addressed to your device. This can be useful when discovering services offered nearby. It uses more power than the non-multicast mode.'
                                    ],
    'android.permission.VIBRATE': ['normal', 'control vibrator',
                'Allows the application to control the vibrator.'],
    'android.permission.FLASHLIGHT': ['normal', 'control flashlight',
                   'Allows the application to control the flashlight.'
                   ],
    'android.permission.WAKE_LOCK': ['normal', 'prevent phone from sleeping',
                  'Allows an application to prevent the phone from going to sleep.'
                  ],
    'android.permission.TRANSMIT_IR': ['normal', 'transmit infrared', "Allows the app to use the phone's infrared transmitter."],
    'android.permission.MODIFY_AUDIO_SETTINGS': ['normal', 'change your audio settings',
                              'Allows application to modify global audio settings, such as volume and routing.'
                              ],
    'android.permission.MANAGE_USB': ['signatureOrSystem', 'manage preferences and permissions for USB devices',
                     'Allows the app to manage preferences and permissions for USB devices.'
                     ],
    'android.permission.ACCESS_MTP': ['signatureOrSystem',
                   'access the MTP USB kernel driver',
                   'Allows an application to access the MTP USB kernel driver. For use only by the device side MTP implementation.'
                   ],
    'android.permission.HARDWARE_TEST': ['signature', 'test hardware',
                      'Allows the application to control various peripherals for the purpose of hardware testing.'
                      ],
    'android.permission.ACCESS_FM_RADIO': ['signatureOrSystem', 'access FM radio', 'Allows the app to access FM radio to listen to programmes.'],
    'android.permission.NET_ADMIN': ['signature',
                  'configure network interfaces, configure/use IPSec, etc'
                  ,
                  'Allows access to configure network interfaces, configure/use IPSec, etc.'
                  ],
    'android.permission.REMOTE_AUDIO_PLAYBACK': ['signature', 'remote audio playback',
                              'Allows registration for remote audio playback'
                              ],
    'android.permission.TV_INPUT_HARDWARE': ['signatureOrSystem', 'hide', "Allows TvInputService to access underlying TV input hardware such as built-in tuners and HDMI-in's."],
    'android.permission.CAPTURE_TV_INPUT': ['signatureOrSystem', 'hide', "Allows to capture a frame of TV input hardware such as built-in tuners and HDMI-in's."],
    'android.permission.OEM_UNLOCK_STATE': ['signature', 'hide', 'Allows enabling/disabling OEM unlock. Not for use by third-party applications.'],
    'android.permission.ACCESS_PDB_STATE': ['signature', 'hide', 'Allows querying state of PersistentDataBlock. Not for use by third-party applications'],
    'android.permission.RECORD_AUDIO': ['dangerous', 'record audio',
                     'Allows application to access the audio record path.'
                     ],
    'android.permission.CAMERA': ['dangerous', 'take pictures and videos',
               'Allows application to take pictures and videos with the camera. This allows the application to collect images that the camera is seeing at any time.'
               ],
    'android.permission.CAMERA_DISABLE_TRANSMIT_LED': ['signatureOrSystem', 'disable transmit indicator LED when camera is in use', 'Allows a pre-installed system application to disable the camera use indicator LED.'],
    'android.permission.PROCESS_OUTGOING_CALLS': ['dangerous', 'intercept outgoing calls',
                               'Allows application to process outgoing calls and change the number to be dialled. Malicious applications may monitor, redirect or prevent outgoing calls.'
                               ],
    'android.permission.MODIFY_PHONE_STATE': ['signatureOrSystem', 'modify phone status',
                           'Allows modification of the telephony state - power on, mmi, etc. Does not include placing calls.'
                           ],
    'android.permission.READ_PHONE_STATE': ['dangerous', 'read phone state and identity',
                         'Allows the application to access the phone features of the device. An application with this permission can determine the phone number and serial number of this phone, whether a call is active, the number that call is connected to and so on.'
                         ],
    'android.permission.READ_PRECISE_PHONE_STATE': ['signatureOrSystem', 'read precise phone states', 'Allows the app to access the precise phone states. This permission allows the app to determine the real call status, whether a call is active or in the background, call fails, precise data connection status and data connection fails.'],
    'android.permission.READ_PRIVILEGED_PHONE_STATE': ['signatureOrSystem',
                                    'read access to privileged phone state',
                                    'Allows read access to privileged phone state.'
                                    ],
    'android.permission.CALL_PHONE': ['dangerous', 'directly call phone numbers',
                   'Allows an application to initiate a phone call without going through the Dialer user interface for the user to confirm the call being placed. '
                   ],
    'android.permission.USE_SIP': ['dangerous', 'make/receive Internet calls',
                'Allows an application to use the SIP service to make/receive Internet calls.'
                ],
    'android.permission.REGISTER_SIM_SUBSCRIPTION': ['signatureOrSystem', 'register new telecom SIM connections', 'Allows the app to register new telecom SIM connections.'],
    'android.permission.REGISTER_CALL_PROVIDER': ['signatureOrSystem', 'register new telecom connections', 'Allows the app to register new telecom connections.'],
    'android.permission.REGISTER_CONNECTION_MANAGER': ['signatureOrSystem', 'manage telecom connections', 'Allows the app to manage telecom connections.'],
    'android.permission.BIND_INCALL_SERVICE': ['signatureOrSystem', 'nteract with in-call screen', 'Allows the app to control when and how the user sees the in-call screen.'],
    'android.permission.BIND_CONNECTION_SERVICE': ['signatureOrSystem', 'interact with telephony services', 'Allows the app to interact with telephony services to make/receive calls.'],
    'android.permission.CONTROL_INCALL_EXPERIENCE': ['signatureOrSystem', 'provide an in-call user experience', 'Allows the app to provide an in-call user experience.'],
    'android.permission.READ_EXTERNAL_STORAGE': ['normal', 'read from external storage',
                              'Allows an application to read from external storage'
                              ],
    'android.permission.WRITE_EXTERNAL_STORAGE': ['dangerous',
                               'modify/delete SD card contents',
                               'Allows an application to write to the SD card.'
                               ],
    'android.permission.WRITE_MEDIA_STORAGE': ['signatureOrSystem',
                            'write to internal media storage',
                            'Allows an application to write to internal media storage'
                            ],
    'android.permission.MANAGE_DOCUMENTS': ['signature', 'manage document storage', 'Allows the app to manage document storage.'],
    'android.permission.DISABLE_KEYGUARD': ['dangerous', 'disable key lock',
                         'Allows an application to disable the key lock and any associated password security. A legitimate example of this is the phone disabling the key lock when receiving an incoming phone call, then re-enabling the key lock when the call is finished.'
                         ],
    'android.permission.GET_TASKS': ['dangerous', 'retrieve running applications',
                  'Allows application to retrieve information about currently and recently running tasks. May allow malicious applications to discover private information about other applications.'
                  ],
    'android.permission.REAL_GET_TASKS': ['signatureOrSystem', 'retrieve running apps', 'Allows the app to retrieve information about currently and recently running tasks. This may allow the app to discover information about which applications are used on the device.'],
    'android.permission.START_TASKS_FROM_RECENTS': ['signatureOrSystem', 'start a task from recents', 'Allows the app to use an ActivityManager.RecentTaskInfo object to launch a defunct task that was returned from ActivityManager.getRecentTaskList().'],
    'android.permission.INTERACT_ACROSS_USERS': ['signatureOrSystemOrDevelopment', '',
                              'Allows an application to call APIs that allow it to do interactions across the users on the device, using singleton services and user-targeted broadcasts.  This permission is not available to third party applications.'
                              ],
    'android.permission.INTERACT_ACROSS_USERS_FULL': ['signature', '',
                                   'Fuller form of INTERACT_ACROSS_USERS that removes restrictions on where broadcasts can be sent and allows other types of interactions.'
                                   ],
    'android.permission.MANAGE_USERS': ['signatureOrSystem', 'manage users', 'Allows apps to manage users on the device, including query, creation and deletion.'],
    'android.permission.GET_DETAILED_TASKS': ['signature', 'retrieve details of running apps',
                           'Allows an application to get full detailed information about recently running tasks, with full fidelity to the real state.'
                           ],
    'android.permission.REORDER_TASKS': ['normal', 'reorder applications running',
                      'Allows an application to move tasks to the foreground and background. Malicious applications can force themselves to the front without your control.'
                      ],
    'android.permission.REMOVE_TASKS': ['signature', '',
                     'Allows an application to change to remove/kill tasks'
                     ],
    'android.permission.MANAGE_ACTIVITY_STACKS': ['signatureOrSystem', 'manage activity stacks', 'Allows the app to add, remove and modify the activity stacks in which other apps run. Malicious apps may disrupt the behaviour of other apps.'],
    'android.permission.START_ANY_ACTIVITY': ['signature', 'start any activity',
                           'Allows an application to start any activity, regardless of permission protection or exported state.'
                           ],
    'android.permission.RESTART_PACKAGES': ['normal', 'kill background processes',
                         'Allows an application to kill background processes of other applications, even if memory is not low.'
                         ],
    'android.permission.KILL_BACKGROUND_PROCESSES': ['normal', 'kill background processes',
                                  'Allows an application to kill background processes of other applications, even if memory is not low.'
                                  ],
    'android.permission.SYSTEM_ALERT_WINDOW': ['dangerous', 'display system-level alerts',
                            'Allows an application to show system-alert windows. Malicious applications can take over the entire screen of the phone.'
                            ],
    'android.permission.SET_WALLPAPER': ['normal', 'set wallpaper',
                      'Allows the application to set the system wallpaper.'
                      ],
    'android.permission.SET_WALLPAPER_HINTS': ['normal', 'set wallpaper size hints',
                            'Allows the application to set the system wallpaper size hints.'
                            ],
    'android.permission.SET_TIME': ['signatureOrSystem', 'set time',
                 "Allows an application to change the phone's clock time."
                 ],
    'android.permission.SET_TIME_ZONE': ['normal', 'set time zone',
                      "Allows an application to change the phone's time zone."
                      ],
    'android.permission.EXPAND_STATUS_BAR': ['normal', 'expand/collapse status bar',
                          'Allows application to expand or collapse the status bar.'
                          ],
    'com.android.launcher.permission.INSTALL_SHORTCUT': ['dangerous', 'install shortcuts', 'Allows an application to add Home screen shortcuts without user intervention.'],
    'com.android.launcher.permission.UNINSTALL_SHORTCUT': ['dangerous', 'uninstall shortcuts', 'Allows the application to remove Home screen shortcuts without user intervention.'],
    'android.permission.READ_SYNC_SETTINGS': ['normal', 'read sync settings',
                           'Allows an application to read the sync settings, such as whether sync is enabled for Contacts.'
                           ],
    'android.permission.WRITE_SYNC_SETTINGS': ['normal', 'write sync settings',
                            'Allows an application to modify the sync settings, such as whether sync is enabled for Contacts.'
                            ],
    'android.permission.READ_SYNC_STATS': ['normal', 'read sync statistics',
                        'Allows an application to read the sync stats; e.g. the history of syncs that have occurred.'
                        ],
    'android.permission.SET_SCREEN_COMPATIBILITY': ['signature', '',
                                 'Change the screen compatibility mode of applications'
                                 ],
    'android.permission.ACCESS_ALL_EXTERNAL_STORAGE': ['signature', 'access external storage of all users',
                                    'Allows an application to access all multi-user external storage'
                                    ],
    'android.permission.CHANGE_CONFIGURATION': ['signatureOrSystemOrDevelopment',
                             'change your UI settings',
                             'Allows an application to change the current configuration, such as the locale or overall font size.'
                             ],
    'android.permission.WRITE_SETTINGS': ['normal', 'modify global system settings',
                       "Allows an application to modify the system\'s settings data. Malicious applications can corrupt your system\'s configuration."
                       ],
    'android.permission.WRITE_GSERVICES': ['signatureOrSystem',
                        'modify the Google services map',
                        'Allows an application to modify the Google services map. Not for use by normal applications.'
                        ],
    'android.permission.FORCE_STOP_PACKAGES': ['signature', 'force-stop other applications'
                            ,
                            'Allows an application to stop other applications forcibly.'
                            ],
    'android.permission.RETRIEVE_WINDOW_CONTENT': ['signatureOrSystem', '',
                                'Allows an application to retrieve the content of the active window An active window is the window that has fired an accessibility event. '
                                ],
    'android.permission.SET_ANIMATION_SCALE': ['signatureOrSystemOrDevelopment',
                            'modify global animation speed',
                            'Allows an application to change the global animation speed (faster or slower animations) at any time.'
                            ],
    'android.permission.PERSISTENT_ACTIVITY': ['normal', 'make application always run',
                            "Allows an application to make parts of itself persistent, so that the system can\'t use it for other applications."
                            ],
    'android.permission.GET_PACKAGE_SIZE': ['normal', 'measure application storage space',
                         'Allows an application to retrieve its code, data and cache sizes'
                         ],
    'android.permission.SET_PREFERRED_APPLICATIONS': ['signature',
                                   'set preferred applications',
                                   'Allows an application to modify your preferred applications. This can allow malicious applications to silently change the applications that are run, spoofing your existing applications to collect private data from you.'
                                   ],
    'android.permission.RECEIVE_BOOT_COMPLETED': ['normal', 'automatically start at boot',
                               'Allows an application to start itself as soon as the system has finished booting. This can make it take longer to start the phone and allow the application to slow down the overall phone by always running.'
                               ],
    'android.permission.BROADCAST_STICKY': ['normal', 'send sticky broadcast',
                         'Allows an application to send sticky broadcasts, which remain after the broadcast ends. Malicious applications can make the phone slow or unstable by causing it to use too much memory.'
                         ],
    'android.permission.MOUNT_UNMOUNT_FILESYSTEMS': ['signatureOrSystem',
                                  'mount and unmount file systems',
                                  'Allows the application to mount and unmount file systems for removable storage.'
                                  ],
    'android.permission.MOUNT_FORMAT_FILESYSTEMS': ['signatureOrSystem',
                                 'format external storage',
                                 'Allows the application to format removable storage.'
                                 ],
    'android.permission.ASEC_ACCESS': ['signature', 'get information on internal storage',
                    'Allows the application to get information on internal storage.'
                    ],
    'android.permission.ASEC_CREATE': ['signature', 'create internal storage',
                    'Allows the application to create internal storage.'
                    ],
    'android.permission.ASEC_DESTROY': ['signature', 'destroy internal storage',
                     'Allows the application to destroy internal storage.'
                     ],
    'android.permission.ASEC_MOUNT_UNMOUNT': ['signature', 'mount/unmount internal storage'
                           ,
                           'Allows the application to mount/unmount internal storage.'
                           ],
    'android.permission.ASEC_RENAME': ['signature', 'rename internal storage',
                    'Allows the application to rename internal storage.'
                    ],
    'android.permission.WRITE_APN_SETTINGS': ['signatureOrSystem',
                           'write Access Point Name settings',
                           'Allows an application to modify the APN settings, such as Proxy and Port of any APN.'
                           ],
    'android.permission.SUBSCRIBED_FEEDS_READ': ['normal', 'read subscribed feeds',
                              'Allows an application to receive details about the currently synced feeds.'
                              ],
    'android.permission.SUBSCRIBED_FEEDS_WRITE': ['dangerous', 'write subscribed feeds',
                               'Allows an application to modify your currently synced feeds. This could allow a malicious application to change your synced feeds.'
                               ],
    'android.permission.CHANGE_NETWORK_STATE': ['normal', 'change network connectivity',
                             'Allows an application to change the state of network connectivity.'
                             ],
    'android.permission.CLEAR_APP_CACHE': ['dangerous', 'delete all application cache data',
                        'Allows an application to free phone storage by deleting files in application cache directory. Access is usually very restricted to system process.'
                        ],
    'android.permission.ALLOW_ANY_CODEC_FOR_PLAYBACK': ['signatureOrSystem', '',
            'Allows an application to use any media decoder when decoding for playback.'
            ],
    'android.permission.MANAGE_CA_CERTIFICATES': ['signatureOrSystem', 'manage trusted credentials', 'Allows the app to install and uninstall CA certificates as trusted credentials.'],
    'android.permission.RECOVERY': ['signatureOrSystem', 'Interact with update and recovery system', 'Allows an application to interact with the recovery system and system updates.'],
    'android.permission.BIND_JOB_SERVICE': ['signature', "run the application's scheduled background work", 'This permission allows the Android system to run the application in the background when requested.'],
    'android.permission.WRITE_SECURE_SETTINGS': ['signatureOrSystemOrDevelopment',
                              'modify secure system settings',
                              "Allows an application to modify the system\'s secure settings data. Not for use by normal applications."
                              ],
    'android.permission.DUMP': ['signatureOrSystemOrDevelopment',
             'retrieve system internal status',
             'Allows application to retrieve internal status of the system. Malicious applications may retrieve a wide variety of private and secure information that they should never normally need.'
             ],
    'android.permission.READ_LOGS': ['signatureOrSystemOrDevelopment',
                  'read sensitive log data',
                  "Allows an application to read from the system\'s various log files. This allows it to discover general information about what you are doing with the phone, potentially including personal or private information."
                  ],
    'android.permission.SET_DEBUG_APP': ['signatureOrSystemOrDevelopment',
                      'enable application debugging',
                      'Allows an application to turn on debugging for another application. Malicious applications can use this to kill other applications.'
                      ],
    'android.permission.SET_PROCESS_LIMIT': ['signatureOrSystemOrDevelopment',
                          'limit number of running processes',
                          'Allows an application to control the maximum number of processes that will run. Never needed for normal applications.'
                          ],
    'android.permission.SET_ALWAYS_FINISH': ['signatureOrSystemOrDevelopment',
                          'make all background applications close',
                          'Allows an application to control whether activities are always finished as soon as they go to the background. Never needed for normal applications.'
                          ],
    'android.permission.SIGNAL_PERSISTENT_PROCESSES': ['signatureOrSystemOrDevelopment',
                                    'send Linux signals to applications',
                                    'Allows application to request that the supplied signal be sent to all persistent processes.'
                                    ],
    'android.permission.DIAGNOSTIC': ['signature', 'read/write to resources owned by diag',
                   'Allows an application to read and write to any resource owned by the diag group; for example, files in /dev. This could potentially affect system stability and security. This should ONLY be used for hardware-specific diagnostics by the manufacturer or operator.'],
    'android.permission.STATUS_BAR': ['signatureOrSystem', 'disable or modify status bar', 'Allows the app to disable the status bar or add and remove system icons.'],
    'android.permission.STATUS_BAR_SERVICE': ['signature', 'status bar',
                           'Allows the application to be the status bar.'],
    'android.permission.FORCE_BACK': ['signature', 'force application to close',
                   'Allows an application to force any activity that is in the foreground to close and go back. Should never be needed for normal applications.'
                   ],
    'android.permission.UPDATE_DEVICE_STATS': ['signatureOrSystem',
                            'modify battery statistics',
                            'Allows the modification of collected battery statistics. Not for use by normal applications.'
                            ],
    'android.permission.GET_APP_OPS_STATS': ['signatureOrSystemOrDevelopment', 'retrieve app ops statistics', 'Allows the app to retrieve collected application operation statistics. Not for use by normal apps.'],
    'android.permission.UPDATE_APP_OPS_STATS': ['signatureOrSystem', 'modify app ops statistics', 'Allows the app to modify collected component usage statistics. Not for use by normal apps.'],
    'android.permission.INTERNAL_SYSTEM_WINDOW': ['signature',
                               'display unauthorised windows',
                               'Allows the creation of windows that are intended to be used by the internal system user interface. Not for use by normal applications.'
                               ],
    'android.permission.MANAGE_APP_TOKENS': ['signature', 'manage application tokens',
                          'Allows applications to create and manage their own tokens, bypassing their normal Z-ordering. Should never be needed for normal applications.'
                          ],
    'android.permission.FREEZE_SCREEN': ['signature', '',
                      'Allows the application to temporarily freeze the screen for a full-screen transition.'
                      ],
    'android.permission.INJECT_EVENTS': ['signature', 'inject user events',
                      'Allows an application to inject user events (keys, touch, trackball) into the event stream and deliver them to ANY window.  Without this permission, you can only deliver events to windows in your own process. Very few applications should need to use this permission'
                      ],
    'android.permission.FILTER_EVENTS': ['signature', '',
                      'Allows an application to register an input filter which filters the stream of user events (keys, touch, trackball) before they are dispatched to any window'
                      ],
    'android.permission.RETRIEVE_WINDOW_TOKEN': ['signature', 'retrieve window token', 'Allows an application to retrieve the window token. Malicious apps may perform unauthorised interaction with the application window impersonating the system.'],
    'android.permission.FRAME_STATS': ['signature', 'retrieve frame statistics', 'Allows an application to collect frame statistics. Malicious apps may observe the frame statistics of windows from other apps.'],
    'android.permission.TEMPORARY_ENABLE_ACCESSIBILITY': ['signature', 'temporary enable accessibility',
            'Allows an application to temporarily enable accessibility on the device. Malicious apps may enable accessibility without user consent.'],
    'android.permission.SET_ACTIVITY_WATCHER': ['signature',
                             'monitor and control all application launching',
                             'Allows an application to monitor and control how the system launches activities. Malicious applications may compromise the system completely. This permission is needed only for development, never for normal phone usage.'
                             ],
    'android.permission.SHUTDOWN': ['signatureOrSystem', 'partial shutdown',
                 'Puts the activity manager into a shut-down state. Does not perform a complete shut down.'
                 ],
    'android.permission.STOP_APP_SWITCHES': ['signatureOrSystem', 'prevent app switches',
                          'Prevents the user from switching to another application.'
                          ],
    'android.permission.GET_TOP_ACTIVITY_INFO': ['signature', 'get current app info', 'Allows the holder to retrieve private information about the current application in the foreground of the screen.'],
    'android.permission.READ_INPUT_STATE': ['signature',
                         'record what you type and actions that you take'
                         ,
                         'Allows applications to watch the keys that you press even when interacting with another application (such as entering a password). Should never be needed for normal applications.'
                         ],
    'android.permission.BIND_INPUT_METHOD': ['signature', 'bind to an input method',
                          'Allows the holder to bind to the top-level interface of an input method. Should never be needed for normal applications.'
                          ],
    'android.permission.BIND_ACCESSIBILITY_SERVICE': ['signature', '',
                                   'Must be required by an android.accessibilityservice.AccessibilityService to ensure that only the system can bind to it. '
                                   ],
    'android.permission.BIND_PRINT_SERVICE': ['signature', 'bind to a print service', 'Allows the holder to bind to the top-level interface of a print service. Should never be needed for normal apps.'],
    'android.permission.BIND_NFC_SERVICE': ['signature', 'bind to NFC service', 'Allows the holder to bind to applications that are emulating NFC cards. Should never be needed for normal apps.'],
    'android.permission.BIND_PRINT_SPOOLER_SERVICE': ['signature', 'bind to a print spooler service', 'Allows the holder to bind to the top-level interface of a print spooler service. Should never be needed for normal apps.'],
    'android.permission.BIND_TEXT_SERVICE': ['signature', '',
                          'Must be required by a TextService (e.g. SpellCheckerService) to ensure that only the system can bind to it.'
                          ],
    'android.permission.BIND_VPN_SERVICE': ['signature', '',
                         'Must be required by an {@link android.net.VpnService}, to ensure that only the system can bind to it.'
                         ],
    'android.permission.BIND_WALLPAPER': ['signatureOrSystem', 'bind to wallpaper',
                       'Allows the holder to bind to the top-level interface of wallpaper. Should never be needed for normal applications.'
                       ],
    'android.permission.BIND_VOICE_INTERACTION': ['signature', 'bind to a voice interactor', 'Allows the holder to bind to the top-level interface of a voice interaction service. Should never be needed for normal apps.'],
    'android.permission.MANAGE_VOICE_KEYPHRASES': ['signatureOrSystem', 'manage voice key phrases', 'Allows the holder to manage the key phrases for voice hotword detection. Should never be needed for normal apps.'],
    'android.permission.BIND_REMOTE_DISPLAY': ['signature', 'bind to a remote display', 'Allows the holder to bind to the top-level interface of a remote display. Should never be needed for normal apps.'],
    'android.permission.BIND_TV_INPUT': ['signatureOrSystem', 'bind to a TV input', 'Allows the holder to bind to the top-level interface of a TV input. Should never be needed for normal apps.'],
    'android.permission.MODIFY_PARENTAL_CONTROLS': ['signatureOrSystem', 'modify parental controls', 'Allows the holder to modify the system\'s parental controls data. Should never be needed for normal apps.'],
    'android.permission.BIND_DEVICE_ADMIN': ['signature', 'interact with device admin', 'Allows the holder to send intents to a device administrator. Should never be needed for normal apps.'],
    'android.permission.MANAGE_DEVICE_ADMINS': ['signatureOrSystem', 'add or remove a device admin', 'Allows the holder to add or remove active device administrators. Should never be needed for normal apps.'],
    'android.permission.SET_ORIENTATION': ['signature', 'change screen orientation',
                        'Allows an application to change the rotation of the screen at any time. Should never be needed for normal applications.'
                        ],
    'android.permission.SET_POINTER_SPEED': ['signature', '',
                          'Allows low-level access to setting the pointer speed. Not for use by normal applications. '
                          ],
    'android.permission.SET_INPUT_CALIBRATION': ['signature', 'change input device calibration', 'Allows the app to modify the calibration parameters of the touch screen. Should never be needed for normal apps.'],
    'android.permission.SET_KEYBOARD_LAYOUT': ['signature', '',
                            'Allows low-level access to setting the keyboard layout. Not for use by normal applications.'
                            ],
    'android.permission.INSTALL_PACKAGES': ['signatureOrSystem',
                         'directly install applications',
                         'Allows an application to install new or updated Android packages. Malicious applications can use this to add new applications with arbitrarily powerful permissions.'
                         ],
    'android.permission.CLEAR_APP_USER_DATA': ['signature',
                            "delete other applications\' data",
                            'Allows an application to clear user data.'
                            ],
    'android.permission.DELETE_CACHE_FILES': ['signatureOrSystem',
                           "delete other applications\' caches",
                           'Allows an application to delete cache files.'
                           ],
    'android.permission.DELETE_PACKAGES': ['signatureOrSystem', 'delete applications',
                        'Allows an application to delete Android packages. Malicious applications can use this to delete important applications.'
                        ],
    'android.permission.MOVE_PACKAGE': ['signatureOrSystem', 'Move application resources',
                     'Allows an application to move application resources from internal to external media and vice versa.'
                     ],
    'android.permission.CHANGE_COMPONENT_ENABLED_STATE': ['signatureOrSystem',
            'enable or disable application components',
            'Allows an application to change whether or not a component of another application is enabled. Malicious applications can use this to disable important phone capabilities. It is important to be careful with permission, as it is possible to bring application components into an unusable, inconsistent or unstable state.'
            ],
    'android.permission.GRANT_REVOKE_PERMISSIONS': ['signature', '',
                                 'Allows an application to grant or revoke specific permissions.'
                                 ],
    'android.permission.ACCESS_SURFACE_FLINGER': ['signature', 'access SurfaceFlinger',
                               'Allows application to use SurfaceFlinger low-level features.'
                               ],
    'android.permission.READ_FRAME_BUFFER': ['signatureOrSystem', 'read frame buffer',
                          'Allows application to read the content of the frame buffer.'
                          ],
    'android.permission.ACCESS_INPUT_FLINGER': ['signature', 'access InputFlinger', 'Allows the app to use InputFlinger low-level features.'],
    'android.permission.CONFIGURE_WIFI_DISPLAY': ['signature', '',
                               'Allows an application to configure and connect to Wifi displays'
                               ],
    'android.permission.CONTROL_WIFI_DISPLAY': ['signature', '',
                             'Allows an application to control low-level features of Wifi displays such as opening an RTSP socket.  This permission should only be used by the display manager.'
                             ],
    'android.permission.CONTROL_VPN': ['signatureOrSystem', 'control Virtual Private Networks', 'Allows the app to control low-level features of Virtual Private Networks.'],
    'android.permission.CAPTURE_AUDIO_OUTPUT': ['signatureOrSystem', 'capture audio output', 'Allows the app to capture and redirect audio output.'],
    'android.permission.CAPTURE_AUDIO_HOTWORD': ['signatureOrSystem', 'Audio Routing', 'Allows the app to directly control audio routing and override audio policy decisions.'],
    'android.permission.CAPTURE_VIDEO_OUTPUT': ['signatureOrSystem', 'capture video output', 'Allows the app to capture and redirect video output.'],
    'android.permission.CAPTURE_SECURE_VIDEO_OUTPUT': ['signatureOrSystem', 'capture secure video output', 'Allows the app to capture and redirect secure video output.'],
    'android.permission.MEDIA_CONTENT_CONTROL': ['signatureOrSystem', 'control media playback and metadata access', 'Allows the app to control media playback and access the media information (title, author...).'],
    'android.permission.BRICK': ['signature', 'permanently disable phone',
              'Allows the application to disable the entire phone permanently. This is very dangerous.'
              ],
    'android.permission.REBOOT': ['signatureOrSystem', 'force phone reboot',
               'Allows the application to force the phone to reboot.'],
    'android.permission.DEVICE_POWER': ['signature', 'turn phone on or off',
                     'Allows the application to turn the phone on or off.'
                     ],
    'android.permission.USER_ACTIVITY': ['signatureOrSystem', 'reset display timeout', 'Allows the app to reset the display timeout.'],
    'android.permission.NET_TUNNELING': ['signature', '',
                      'Allows low-level access to tun tap driver '],
    'android.permission.FACTORY_TEST': ['signature', 'run in factory test mode',
                     'Run as a low-level manufacturer test, allowing complete access to the phone hardware. Only available when a phone is running in manufacturer test mode.'
                     ],
    'android.permission.BROADCAST_PACKAGE_REMOVED': ['signature',
                                  'send package removed broadcast',
                                  'Allows an application to broadcast a notification that an application package has been removed. Malicious applications may use this to kill any other application running.'
                                  ],
    'android.permission.BROADCAST_SMS': ['signature', 'send SMS-received broadcast',
                      'Allows an application to broadcast a notification that an SMS message has been received. Malicious applications may use this to forge incoming SMS messages.'
                      ],
    'android.permission.BROADCAST_WAP_PUSH': ['signature',
                           'send WAP-PUSH-received broadcast',
                           'Allows an application to broadcast a notification that a WAP-PUSH message has been received. Malicious applications may use this to forge MMS message receipt or to replace the content of any web page silently with malicious variants.'
                           ],
    'android.permission.BROADCAST_NETWORK_PRIVILEGED': ['signatureOrSystem', 'hide', 'Allows an application to broadcast privileged networking requests.'],
    'android.permission.MASTER_CLEAR': ['signatureOrSystem',
                     'reset system to factory defaults',
                     'Allows an application to completely reset the system to its factory settings, erasing all data, configuration and installed applications.'
                     ],
    'android.permission.CALL_PRIVILEGED': ['signatureOrSystem',
                        'directly call any phone numbers',
                        'Allows the application to call any phone number, including emergency numbers, without your intervention. Malicious applications may place unnecessary and illegal calls to emergency services.'
                        ],
    'android.permission.PERFORM_CDMA_PROVISIONING': ['signatureOrSystem',
                                  'directly start CDMA phone setup',
                                  'Allows the application to start CDMA provisioning. Malicious applications may start CDMA provisioning unnecessarily'
                                  ],
    'android.permission.CONTROL_LOCATION_UPDATES': ['signatureOrSystem',
                                 'control location update notifications'
                                 ,
                                 'Allows enabling/disabling location update notifications from the radio. Not for use by normal applications.'
                                 ],
    'android.permission.ACCESS_CHECKIN_PROPERTIES': ['signatureOrSystem',
                                  'access check-in properties',
                                  'Allows read/write access to properties uploaded by the check-in service. Not for use by normal applications.'
                                  ],
    'android.permission.PACKAGE_USAGE_STATS': ['signatureOrSystem',
                            'update component usage statistics',
                            'Allows the modification of collected component usage statistics. Not for use by normal applications.'
                            ],
    'android.permission.BATTERY_STATS': ['signatureOrSystemOrDevelopment', 'modify battery statistics',
                      'Allows the modification of collected battery statistics. Not for use by normal applications.'
                      ],
    'android.permission.BACKUP': ['signatureOrSystem', 'control system back up and restore'
               ,
               "Allows the application to control the system\'s back-up and restore mechanism. Not for use by normal applications."
               ],
    'android.permission.CONFIRM_FULL_BACKUP': ['signature', '',
                            'Allows a package to launch the secure full-backup confirmation UI. ONLY the system process may hold this permission.'
                            ],
    'android.permission.BIND_REMOTEVIEWS': ['signatureOrSystem', '',
                         'Must be required by a {@link android.widget.RemoteViewsService}, to ensure that only the system can bind to it.'
                         ],
    'android.permission.BIND_APPWIDGET': ['signatureOrSystem', 'choose widgets',
                       'Allows the application to tell the system which widgets can be used by which application. With this permission, applications can give access to personal data to other applications. Not for use by normal applications.'
                       ],
    'android.permission.BIND_KEYGUARD_APPWIDGET': ['signatureOrSystem', '',
                                'Private permission, to restrict who can bring up a dialog to add a new keyguard widget'
                                ],
    'android.permission.MODIFY_APPWIDGET_BIND_PERMISSIONS': ['signatureOrSystem',
            'query/set which applications can bind AppWidgets.',
            'Internal permission allowing an application to query/set which applications can bind AppWidgets.'
            ],
    'android.permission.CHANGE_BACKGROUND_DATA_SETTING': ['signature',
            'change background data usage setting',
            'Allows an application to change the background data usage setting.'
            ],
    'android.permission.GLOBAL_SEARCH': ['signatureOrSystem', '',
                      'This permission can be used on content providers to allow the global search system to access their data.  Typically it used when the provider has some permissions protecting it (which global search would not be expected to hold),and added as a read-only permission to the path in the provider where global search queries are performed.  This permission can not be held by regular applications; it is used by applications to protect themselves from everyone else besides global search'
                      ],
    'android.permission.GLOBAL_SEARCH_CONTROL': ['signature', '',
                              'Internal permission protecting access to the global search system: ensures that only the system can access the provider to perform queries (since this otherwise provides unrestricted access to a variety of content providers), and to write the search statistics (to keep applications from gaming the source ranking).'
                              ],
    'android.permission.READ_SEARCH_INDEXABLES': ['signatureOrSystem', 'hide', 'Internal permission to allows an application to read indexable data.'],
    'android.permission.SET_WALLPAPER_COMPONENT': ['signatureOrSystem',
                                'set a live wallpaper',
                                'Allows applications to set a live wallpaper.'
                                ],
    'android.permission.READ_DREAM_STATE': ['signature', '',
                         'Allows applications to read dream settings and dream state.'
                         ],
    'android.permission.WRITE_DREAM_STATE': ['signature', '',
                          'Allows applications to write dream settings, and start or stop dreaming.'
                          ],
    'android.permission.ACCESS_CACHE_FILESYSTEM': ['signatureOrSystem',
                                'access the cache file system',
                                'Allows an application to read and write the cache file system.'
                                ],
    'android.permission.COPY_PROTECTED_DATA': ['signature',
                            'Allows to invoke default container service to copy content. Not for use by normal applications.'
                            ,
                            'Allows to invoke default container service to copy content. Not for use by normal applications.'
                            ],
    'android.permission.CRYPT_KEEPER': ['signatureOrSystem',
                     'access to the encryption methods',
                     'Internal permission protecting access to the encryption methods'
                     ],
    'android.permission.READ_NETWORK_USAGE_HISTORY': ['signatureOrSystem',
                                   'read historical network usage for specific networks and applications.'
                                   ,
                                   'Allows an application to read historical network usage for specific networks and applications.'
                                   ],
    'android.permission.MANAGE_NETWORK_POLICY': ['signature',
                              'manage network policies and to define application-specific rules.'
                              ,
                              'Allows an application to manage network policies and to define application-specific rules.'
                              ],
    'android.permission.MODIFY_NETWORK_ACCOUNTING': ['signatureOrSystem',
                                  'account its network traffic against other UIDs.'
                                  ,
                                  'Allows an application to account its network traffic against other UIDs.'
                                  ],
    'android.permission.C2D_MESSAGE': ['signature', 'C2DM permission.', 'C2DM permission.'
                    ],
    'android.permission.PACKAGE_VERIFICATION_AGENT': ['signatureOrSystem',
                                   'Package verifier needs to have this permission before the PackageManager will trust it to verify packages.'
                                   ,
                                   'Package verifier needs to have this permission before the PackageManager will trust it to verify packages.'
                                   ],
    'android.permission.BIND_PACKAGE_VERIFIER': ['signature', '',
                              'Must be required by package verifier receiver, to ensure that only the system can interact with it..'
                              ],
    'android.permission.SERIAL_PORT': ['signature', '',
                    'Allows applications to access serial ports via the SerialManager.'
                    ],
    'android.permission.ACCESS_CONTENT_PROVIDERS_EXTERNALLY': ['signature', '',
            'Allows the holder to access content providers from outside an ApplicationThread. This permission is enforced by the ActivityManagerService on the corresponding APIs,in particular ActivityManagerService#getContentProviderExternal(String) and ActivityManagerService#removeContentProviderExternal(String).'
            ],
    'android.permission.UPDATE_LOCK': ['signatureOrSystem', '',
                    'Allows an application to hold an UpdateLock, recommending that a headless OTA reboot *not* occur while the lock is held'
                    ],
    'android.permission.ACCESS_KEYGUARD_SECURE_STORAGE': ['signature', 'Access keyguard secure storage', 'Allows an application to access keyguard secure storage.'],
    'android.permission.CONTROL_KEYGUARD': ['signature', 'Control displaying and hiding keyguard', 'Allows an application to control keyguard.'],
    'android.permission.TRUST_LISTENER': ['signature', 'Listen to trust state changes.', 'Allows an application to listen for changes in trust state.'],
    'android.permission.PROVIDE_TRUST_AGENT': ['signatureOrSystem', 'Provide a trust agent.', 'Allows an application to provide a trust agent.'],
    'android.permission.LAUNCH_TRUST_AGENT_SETTINGS': ['signatureOrSystem', 'Launch trust agent settings menu.', 'Allows an application to launch an activity that changes the trust agent behaviour.'],
    'android.permission.BIND_TRUST_AGENT': ['signature', 'Bind to a trust agent service', 'Allows an application to bind to a trust agent service.'],
    'android.permission.BIND_NOTIFICATION_LISTENER_SERVICE': ['signature', 'bind to a notification listener service', 'Allows the holder to bind to the top-level interface of a notification listener service. Should never be needed for normal apps.'],
    'android.permission.BIND_CONDITION_PROVIDER_SERVICE': ['signature', 'bind to a condition provider service', 'Allows the holder to bind to the top-level interface of a condition provider service. Should never be needed for normal apps.'],
    'android.permission.BIND_DREAM_SERVICE': ['signature', 'bind to a dream service', 'Allows the holder to bind to the top-level interface of a dream service. Should never be needed for normal apps.'],
    'android.permission.INVOKE_CARRIER_SETUP': ['signatureOrSystem', 'invoke the carrier-provided configuration app', 'Allows the holder to invoke the carrier-provided configuration app. Should never be needed for normal apps.'],
    'android.permission.ACCESS_NETWORK_CONDITIONS': ['signatureOrSystem', 'listen for observations on network conditions', 'Allows an application to listen for observations on network conditions. Should never be needed for normal apps.'],
    'android.permission.ACCESS_DRM_CERTIFICATES': ['signatureOrSystem', 'access DRM certificates', 'Allows an application to provision and use DRM certficates. Should never be needed for normal apps.'],
    'android.permission.MANAGE_MEDIA_PROJECTION': ['signature', 'Manage media projection sessions', 'Allows an application to manage media projection sessions. These sessions can provide applications with the ability to capture display and audio contents. Should never be needed by normal apps.'],
    'android.permission.READ_INSTALL_SESSIONS': ['', 'Read install sessions', 'Allows an application to read install sessions. This allows it to see details about active package installations.'],
    'android.permission.REMOVE_DRM_CERTIFICATES': ['signatureOrSystem', 'remove DRM certificates', 'Allows an application to remove DRM certficates. Should never be needed for normal apps.'],
    'android.permission.BIND_CARRIER_MESSAGING_SERVICE': ['signatureOrSystem', 'bind to a carrier messaging service', 'Allows the holder to bind to the top-level interface of a carrier messaging service. Should never be needed for normal apps.'],

    }, 'MANIFEST_PERMISSION_GROUP': {
    'COST_MONEY': 'Used for permissions that can be used to make the user spend money without their direct involvement.',
    'MESSAGES': 'Used for permissions that allow an application to send messages on behalf of the user or intercept messages being received by the user.',
    'SOCIAL_INFO': "Used for permissions that provide access to the user's social connections, such as contacts, call logs, social stream, etc.  This includes both reading and writing of this data (which should generally be expressed as two distinct permissions)",
    'PERSONAL_INFO': "Used for permissions that provide access to the user's private data, such as contacts, calendar events, e-mail messages, etc.",
    'CALENDAR': 'Used for permissions that provide access to the device calendar to create / view events',
    'USER_DICTIONARY': 'Used for permissions that provide access to the user calendar to create / view events.',
    'WRITE_USER_DICTIONARY': 'Used for permissions that provide access to the user calendar to create / view events.',
    'BOOKMARKS': 'Used for permissions that provide access to the user bookmarks and browser history.',
    'DEVICE_ALARMS': 'Used for permissions that provide access to the user voicemail box.',
    'VOICEMAIL': 'Used for permissions that provide access to the user voicemail box.',

    'ACCESSIBILITY_FEATURES': 'Used for permissions that allow requesting certain accessibility features.',
    'LOCATION': "Used for permissions that allow access to the user's current location.",
    'NETWORK': 'Used for permissions that provide access to networking services.',
    'BLUETOOTH_NETWORK': 'Used for permissions that provide access to other devices through Bluetooth.',
    'ACCOUNTS': 'Permissions for direct access to the accounts managed by the Account Manager.',
    'AFFECTS_BATTERY': 'Used for permissions that provide direct access to the hardware on the device that has an effect on battery life.  This includes vibrator, flashlight,  etc.',
    'AUDIO_SETTINGS': 'Used for permissions that provide direct access to speaker settings the device.',
    'HARDWARE_CONTROLS': 'Used for permissions that provide direct access to the hardware on the device.',
    'MICROPHONE': 'Used for permissions that are associated with accessing microphone audio from the device. Note that phone calls also capture audio but are in a separate (more visible) permission group.',
    'CAMERA': 'Used for permissions that are associated with accessing camera or capturing images/video from the device.',
    'PHONE_CALLS': 'Used for permissions that are associated with accessing and modifyign telephony state: intercepting outgoing calls, reading and modifying the phone state.',
    'STORAGE': 'Group of permissions that are related to SD card access.',
    'SCREENLOCK': 'Group of permissions that are related to the screenlock.',
    'APP_INFO': 'Group of permissions that are related to the other applications installed on the system.',
    'DISPLAY': 'Group of permissions that allow manipulation of how another application displays UI to the user.',
    'WALLPAPER': 'Group of permissions that allow manipulation of how another application displays UI to the user.',
    'SYSTEM_CLOCK': 'Group of permissions that are related to system clock.',
    'STATUS_BAR': 'Used for permissions that change the status bar.',
    'SYNC_SETTINGS': 'Used for permissions that access the sync settings or sync related information.',
    'SYSTEM_TOOLS': 'Group of permissions that are related to system APIs.',
    'DEVELOPMENT_TOOLS': 'Group of permissions that are related to development features.',
    }}
