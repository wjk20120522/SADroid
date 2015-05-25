PERMISSIONS = {
"android.permission.BIND_WALLPAPER" : {
    "Landroid/service/wallpaper/WallpaperService;" : [
        ("C","SERVICE_INTERFACE","Ljava/lang/String;"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.service.wallpaper.WallpaperService","null"),
    ],
    "Lcom/android/server/WallpaperManagerService;": [
        ("F","bindWallpaperComponentLocked","(Landroid/content/ComponentName;)"),
    ],
},

"android.permission.WRITE_APN_SETTINGS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","insert","Lcom/android/internal/telephony/dataconnection/DcTracker;->PREFERAPN_NO_UPDATE_URI"),
        ("F","update","Lcom/android/internal/telephony/dataconnection/DcTracker;->PREFERAPN_NO_UPDATE_URI"),
        ("F","delete","Lcom/android/internal/telephony/dataconnection/DcTracker;->PREFERAPN_NO_UPDATE_URI"),
        ("F","insert","Landroid/provider/Telephony$Carriers;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Carriers;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Carriers;->CONTENT_URI"),
    ],
},

"android.permission.ACCESS_SURFACE_FLINGER" : {
    "Landroid/view/Surface;" : [
        ("F","closeTransaction","()"),
        ("F","freezeDisplay","(I)"),
        ("F","setOrientation","(I I I)"),
        ("F","setOrientation","(I I)"),
        ("F","unfreezeDisplay","(I)"),
    ],
    "Landroid/view/SurfaceSession;" : [
        ("F","<init>","()"),
    ],
},

"android.permission.READ_INPUT_STATE" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","getDPadKeycodeState","(I)"),
        ("F","getDPadScancodeState","(I)"),
        ("F","getKeycodeState","(I)"),
        ("F","getKeycodeStateForDevice","(I I)"),
        ("F","getScancodeState","(I)"),
        ("F","getScancodeStateForDevice","(I I)"),
        ("F","getSwitchState","(I)"),
        ("F","getSwitchStateForDevice","(I I)"),
        ("F","getTrackballKeycodeState","(I)"),
        ("F","getTrackballScancodeState","(I)"),
    ],
},

"android.permission.READ_SYNC_SETTINGS" : {
    "Landroid/app/ContextImpl$ApplicationContentResolver;" : [
        ("F","getIsSyncable","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getMasterSyncAutomatically","()"),
        ("F","getPeriodicSyncs","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/IContentService$Stub$Proxy;" : [
        ("F","getIsSyncable","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getMasterSyncAutomatically","()"),
        ("F","getPeriodicSyncs","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentService;" : [
        ("F","getIsSyncable","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getMasterSyncAutomatically","()"),
        ("F","getPeriodicSyncs","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","getIsSyncable","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getMasterSyncAutomatically","()"),
        ("F","getPeriodicSyncs","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","getSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
},

"android.permission.FACTORY_TEST" : {
    "Landroid/content/pm/ApplicationInfo;" : [
        ("C","FLAG_FACTORY_TEST","I"),
        ("C","flags","I"),
    ],
    "Landroid/content/Intent;" : [
        ("C","IntentResolution","Ljava/lang/String;"),
        ("C","ACTION_FACTORY_TEST","Ljava/lang/String;"),
    ],
},

"android.permission.FORCE_BACK" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","unhandledBack","(I)"),
    ],
},

"android.permission.READ_CALENDAR" : {
    "Landroid/provider/Calendar$Events;" : [
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/provider/Calendar$EventDays;" : [
        ("F","query","(Landroid/content/ContentResolver; I I)"),
    ],
    "Landroid/provider/Calendar$Calendars;" : [
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.calendar"),
        ("F","query","Lcom/android/calendar/alerts/InitAlarmsService;->SCHEDULE_ALARM_REMOVE_URI"),
        ("F","query","Landroid/provider/CalendarContract$CalendarCache;->URI"),
        ("F","query","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI_BY_INSTANCE"),
        ("F","query","Landroid/provider/CalendarContract$EventDays;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Reminders;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_BY_DAY_URI"),
        ("F","query","Landroid/provider/CalendarContract$Instances;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$SyncState;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_URI"),
        ("F","query","Landroid/provider/CalendarContract$ExtendedProperties;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Instances;->CONTENT_BY_DAY_URI"),
        ("F","query","Landroid/provider/CalendarContract$EventsEntity;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Events;->CONTENT_EXCEPTION_URI"),
        ("F","query","Landroid/provider/CalendarContract$Attendees;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Events;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Calendars;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$Colors;->CONTENT_URI"),
        ("F","query","Landroid/provider/CalendarContract$CalendarEntity;->CONTENT_URI"),
    ],
    "Landroid/provider/Calendar$CalendarAlerts;" : [
        ("F","alarmExists","(Landroid/content/ContentResolver; J J J)"),
        ("F","findNextAlarmTime","(Landroid/content/ContentResolver; J)"),
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"),
    ],
    "Landroid/provider/Calendar$Instances;" : [
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J Ljava/lang/String; Ljava/lang/String;)"),
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; J J)"),
    ],
},

"android.permission.READ_LOGS" : {
    "Lcom/android/internal/os/IDropBoxManagerService$Stub$Proxy;" : [
        ("F","getNextEntry","(Ljava/lang/String; J)"),
    ],
    "Ljava/lang/Runtime;" : [
        ("F","exec","(Ljava/lang/String;)"),
        ("F","exec","([Ljava/lang/String;)"),
        ("F","exec","([Ljava/lang/String; [Ljava/lang/String;)"),
        ("F","exec","([Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)"),
        ("F","exec","(Ljava/lang/String; [Ljava/lang/String;)"),
        ("F","exec","(Ljava/lang/String; [Ljava/lang/String; Ljava/io/File;)"),
    ],
    "Landroid/os/DropBoxManager;" : [
        ("C","ACTION_DROPBOX_ENTRY_ADDED","Ljava/lang/String;"),
        ("F","getNextEntry","(Ljava/lang/String; J)"),
        ("F","getNextEntry","(Ljava/lang/String; J)"),
    ],
},

"android.permission.PROCESS_OUTGOING_CALLS" : {
    "Landroid/content/Intent;" : [
        ("C","ACTION_NEW_OUTGOING_CALL","Ljava/lang/String;"),
    ],
},

"android.permission.BIND_VPN_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.net.VpnService","null"),
    ],
},

"android.permission.CALL_PRIVILEGED" : {
    "Landroid/telephony/PhoneNumberUtils;" : [
        ("F","getNumberFromIntent","(Landroid/content/Intent; Landroid/content/Context;)"),
    ],
    "Landroid/telephony/TelephonyManager;" : [
        ("F","getCompleteVoiceMailNumber","()"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.CALL_EMERGENCY","sip"),
        ("C","android.intent.action.CALL_EMERGENCY","tel"),
        ("C","android.intent.action.CALL_EMERGENCY","vnd.android.cursor.item/phone vnd.android.cursor.item/person"),
        ("C","android.intent.action.CALL_EMERGENCY","voicemail"),
        ("C","android.intent.action.CALL_PRIVILEGED","sip"),
        ("C","android.intent.action.CALL_PRIVILEGED","tel"),
        ("C","android.intent.action.CALL_PRIVILEGED","vnd.android.cursor.item/phone vnd.android.cursor.item/phone_v2 vnd.android.cursor.item/person"),
        ("C","android.intent.action.CALL_PRIVILEGED","voicemail"),
    ],
},

"com.android.gallery3d.filtershow.permission.WRITE" : {
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://com.android.gallery3d.filtershow.provider.SharedImageProvider"),
        ("F","update","content://com.android.gallery3d.filtershow.provider.SharedImageProvider"),
        ("F","delete","content://com.android.gallery3d.filtershow.provider.SharedImageProvider"),
        ("F","insert","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
        ("F","update","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
        ("F","delete","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
    ],
},

"android.permission.READ_SYNC_STATS" : {
    "Landroid/app/ContextImpl$ApplicationContentResolver;" : [
        ("F","getCurrentSync","()"),
        ("F","getSyncStatus","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncActive","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncPending","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/IContentService$Stub$Proxy;" : [
        ("F","getCurrentSync","()"),
        ("F","getSyncStatus","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncActive","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncPending","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentService;" : [
        ("F","getCurrentSync","()"),
        ("F","getSyncStatus","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncActive","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncPending","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","getCurrentSync","()"),
        ("F","getSyncStatus","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncActive","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","isSyncPending","(Landroid/accounts/Account; Ljava/lang/String;)"),
    ],
},

"android.permission.SHUTDOWN" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.ACTION_REQUEST_SHUTDOWN","null"),
        ("C","android.intent.action.REBOOT","null"),
    ],
},

"android.permission.WRITE_CALENDAR" : {
    "Landroid/provider/Calendar$Calendars;" : [
        ("F","delete","(Landroid/content/ContentResolver; Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ("F","deleteCalendarsForAccount","(Landroid/content/ContentResolver; Landroid/accounts/Account;)"),
    ],
    "Landroid/provider/Calendar$CalendarAlerts;" : [
        ("F","insert","(Landroid/content/ContentResolver; J J J J I)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://com.android.calendar"),
        ("F","update","content://com.android.calendar"),
        ("F","delete","content://com.android.calendar"),
        ("F","insert","Lcom/android/calendar/alerts/InitAlarmsService;->SCHEDULE_ALARM_REMOVE_URI"),
        ("F","update","Lcom/android/calendar/alerts/InitAlarmsService;->SCHEDULE_ALARM_REMOVE_URI"),
        ("F","delete","Lcom/android/calendar/alerts/InitAlarmsService;->SCHEDULE_ALARM_REMOVE_URI"),
        ("F","insert","Landroid/provider/CalendarContract$CalendarCache;->URI"),
        ("F","update","Landroid/provider/CalendarContract$CalendarCache;->URI"),
        ("F","delete","Landroid/provider/CalendarContract$CalendarCache;->URI"),
        ("F","insert","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI_BY_INSTANCE"),
        ("F","update","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI_BY_INSTANCE"),
        ("F","delete","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI_BY_INSTANCE"),
        ("F","insert","Landroid/provider/CalendarContract$EventDays;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$EventDays;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$EventDays;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$CalendarAlerts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Reminders;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Reminders;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Reminders;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_BY_DAY_URI"),
        ("F","update","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_BY_DAY_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_BY_DAY_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Instances;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Instances;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Instances;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$SyncState;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$SyncState;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$SyncState;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_URI"),
        ("F","update","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Instances;->CONTENT_SEARCH_URI"),
        ("F","insert","Landroid/provider/CalendarContract$ExtendedProperties;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$ExtendedProperties;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$ExtendedProperties;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Instances;->CONTENT_BY_DAY_URI"),
        ("F","update","Landroid/provider/CalendarContract$Instances;->CONTENT_BY_DAY_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Instances;->CONTENT_BY_DAY_URI"),
        ("F","insert","Landroid/provider/CalendarContract$EventsEntity;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$EventsEntity;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$EventsEntity;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Events;->CONTENT_EXCEPTION_URI"),
        ("F","update","Landroid/provider/CalendarContract$Events;->CONTENT_EXCEPTION_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Events;->CONTENT_EXCEPTION_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Attendees;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Attendees;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Attendees;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Events;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Events;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Events;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Calendars;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Calendars;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Calendars;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$Colors;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$Colors;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$Colors;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CalendarContract$CalendarEntity;->CONTENT_URI"),
        ("F","update","Landroid/provider/CalendarContract$CalendarEntity;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CalendarContract$CalendarEntity;->CONTENT_URI"),
    ],
},

"android.permission.INTERNET" : {
    "Ljava/net/Socket;" : [
        ("F","<init>","()"),
        ("F","<init>","(Ljava/lang/String; I)"),
        ("F","<init>","(Ljava/lang/String; I Ljava/net/InetAddress; I)"),
        ("F","<init>","(Ljava/lang/String; I B)"),
        ("F","<init>","(Ljava/net/InetAddress; I)"),
        ("F","<init>","(Ljava/net/InetAddress; I Ljava/net/InetAddress; I)"),
        ("F","<init>","(Ljava/net/InetAddress; I B)"),
    ],
    "Lorg/apache/http/impl/client/DefaultHttpClient;" : [
        ("F","<init>","()"),
        ("F","<init>","(Lorg/apache/http/params/HttpParams;)"),
        ("F","<init>","(Lorg/apache/http/conn/ClientConnectionManager; Lorg/apache/http/params/HttpParams;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"),
    ],
    "Lcom/android/http/multipart/Part;" : [
        ("F","send","(Ljava/io/OutputStream;)"),
        ("F","sendParts","(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part;)"),
        ("F","sendParts","(Ljava/io/OutputStream; [Lcom/android/http/multipart/Part; [B)"),
        ("F","sendStart","(Ljava/io/OutputStream;)"),
        ("F","sendTransferEncodingHeader","(Ljava/io/OutputStream;)"),
    ],
    "Ljava/net/HttpURLConnection;" : [
        ("F","<init>","(Ljava/net/URL;)"),
        ("F","connect","()"),
    ],
    "Lorg/apache/http/impl/client/HttpClient;" : [
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"),
        ("F","execute","(Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/client/ResponseHandler;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest;)"),
        ("F","execute","(Lorg/apache/http/HttpHost; Lorg/apache/http/client/methods/HttpUriRequest; Lorg/apache/http/protocol/HttpContext;)"),
    ],
    "Lcom/android/http/multipart/FilePart;" : [
        ("F","sendData","(Ljava/io/OutputStream;)"),
        ("F","sendDispositionHeader","(Ljava/io/OutputStream;)"),
    ],
    "Landroid/drm/DrmErrorEvent;" : [
        ("C","TYPE_NO_INTERNET_CONNECTION","I"),
    ],
    "Landroid/webkit/WebViewCore;" : [
        ("F","<init>","(Landroid/content/Context; Landroid/webkit/WebView; Landroid/webkit/CallbackProxy; Ljava/util/Map;)"),
    ],
    "Ljava/net/URLConnection;" : [
        ("F","connect","()"),
        ("F","getInputStream","()"),
    ],
    "Ljava/net/ServerSocket;" : [
        ("F","<init>","()"),
        ("F","<init>","(I)"),
        ("F","<init>","(I I)"),
        ("F","<init>","(I I Ljava/net/InetAddress;)"),
        ("F","bind","(Ljava/net/SocketAddress;)"),
        ("F","bind","(Ljava/net/SocketAddress; I)"),
    ],
    "Ljava/net/NetworkInterface;" : [
        ("F","<init>","()"),
        ("F","<init>","(Ljava/lang/String; I Ljava/net/InetAddress;)"),
    ],
    "Landroid/webkit/WebView;" : [
        ("F","<init>","(Landroid/content/Context; Landroid/util/AttributeSet; I)"),
        ("F","<init>","(Landroid/content/Context; Landroid/util/AttributeSet;)"),
        ("F","<init>","(Landroid/content/Context;)"),
    ],
    "Lcom/android/http/multipart/StringPart;" : [
        ("F","sendData","(Ljava/io/OuputStream;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://downloads/download"),
        ("F","insert","content://downloads/download"),
        ("F","update","content://downloads/download"),
        ("F","delete","content://downloads/download"),
        ("F","query","content://downloads/my_downloads"),
        ("F","insert","content://downloads/my_downloads"),
        ("F","update","content://downloads/my_downloads"),
        ("F","delete","content://downloads/my_downloads"),
        ("F","query","Landroid/provider/Downloads$Impl;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Downloads$Impl;->CONTENT_URI"),
        ("F","update","Landroid/provider/Downloads$Impl;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Downloads$Impl;->CONTENT_URI"),
    ],
    "Landroid/app/Activity;" : [
        ("F","setContentView","(I)"),
    ],
    "Ljava/net/DatagramSocket;" : [
        ("F","<init>","()"),
        ("F","<init>","(I)"),
        ("F","<init>","(I Ljava/net/InetAddress;)"),
        ("F","<init>","(Ljava/net/SocketAddress;)"),
    ],
    "Landroid/webkit/WebSettings;" : [
        ("F","setBlockNetworkLoads","(B)"),
        ("F","verifyNetworkAccess","()"),
    ],
    "Ljava/net/URL;" : [
        ("F","getContent","([Ljava/lang/Class;)"),
        ("F","getContent","()"),
        ("F","openConnection","(Ljava/net/Proxy;)"),
        ("F","openConnection","()"),
        ("F","openStream","()"),
    ],
    "Ljava/net/MulticastSocket;" : [
        ("F","<init>","()"),
        ("F","<init>","(I)"),
        ("F","<init>","(Ljava/net/SocketAddress;)"),
    ],
},

"android.permission.SET_ANIMATION_SCALE" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","setAnimationScale","(I F)"),
        ("F","setAnimationScales","([L;)"),
    ],
},

"android.permission.CHANGE_CONFIGURATION" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","updateConfiguration","(Landroid/content/res/Configuration;)"),
    ],
},

"android.permission.NFC" : {
    "Landroid/nfc/tech/MifareClassic;" : [
        ("C","KEY_NFC_FORUM","[B"),
        ("F","authenticateSectorWithKeyA","(I [B)"),
        ("F","authenticateSectorWithKeyB","(I [B)"),
        ("F","close","()"),
        ("F","connect","()"),
        ("F","decrement","(I I)"),
        ("F","increment","(I I)"),
        ("F","readBlock","(I)"),
        ("F","restore","(I)"),
        ("F","transceive","([B)"),
        ("F","transfer","(I)"),
        ("F","writeBlock","(I [B)"),
    ],
    "Landroid/nfc/tech/TagTechnology;" : [
        ("F","close","()"),
        ("F","connect","()"),
    ],
    "Landroid/nfc/tech/NfcB;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","get","(Landroid/nfc/Tag;)"),
        ("F","transceive","([B)"),
    ],
    "Landroid/nfc/tech/IsoDep;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","setTimeout","(I)"),
        ("F","transceive","([B)"),
    ],
    "Landroid/app/Service;" : [
        ("C","WhatIsAService","I"),
        ("C","ServiceLifecycle","I"),
        ("C","Permissions","I"),
        ("C","ProcessLifecycle","I"),
        ("C","LocalServiceSample","I"),
        ("C","RemoteMessengerServiceSample","I"),
    ],
    "Landroid/nfc/tech/NfcV;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","get","(Landroid/nfc/Tag;)"),
        ("F","transceive","([B)"),
    ],
    "Landroid/nfc/tech/NfcA;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","get","(Landroid/nfc/Tag;)"),
        ("F","transceive","([B)"),
    ],
    "Landroid/nfc/tech/NdefFormatable;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","format","(Landroid/nfc/NdefMessage;)"),
        ("F","formatReadOnly","(Landroid/nfc/NdefMessage;)"),
    ],
    "Landroid/nfc/tech/Ndef;" : [
        ("C","NFC_FORUM_TYPE_1","Ljava/lang/String;"),
        ("C","NFC_FORUM_TYPE_2","Ljava/lang/String;"),
        ("C","NFC_FORUM_TYPE_3","Ljava/lang/String;"),
        ("C","NFC_FORUM_TYPE_4","Ljava/lang/String;"),
        ("F","close","()"),
        ("F","connect","()"),
        ("F","getType","()"),
        ("F","isWritable","()"),
        ("F","makeReadOnly","()"),
        ("F","writeNdefMessage","(Landroid/nfc/NdefMessage;)"),
    ],
    "Landroid/nfc/NfcAdapter;" : [
        ("C","ACTION_TECH_DISCOVERED","Ljava/lang/String;"),
        ("F","disableForegroundDispatch","(Landroid/app/Activity;)"),
        ("F","disableForegroundNdefPush","(Landroid/app/Activity;)"),
        ("F","enableForegroundDispatch","(Landroid/app/Activity; Landroid/app/PendingIntent; [Landroid/content/IntentFilter; [[Ljava/lang/String[];)"),
        ("F","enableForegroundNdefPush","(Landroid/app/Activity; Landroid/nfc/NdefMessage;)"),
        ("F","getDefaultAdapter","()"),
        ("F","getDefaultAdapter","(Landroid/content/Context;)"),
        ("F","isEnabled","()"),
    ],
    "Landroid/app/Activity;" : [
        ("C","Fragments","I"),
        ("C","ActivityLifecycle","I"),
        ("C","ConfigurationChanges","I"),
        ("C","StartingActivities","I"),
        ("C","SavingPersistentState","I"),
        ("C","Permissions","I"),
        ("C","ProcessLifecycle","I"),
    ],
    "Landroid/inputmethodservice/InputMethodService;" : [
        ("C","SoftInputView","I"),
        ("C","CandidatesView","I"),
        ("C","FullscreenMode","I"),
        ("C","GeneratingText","I"),
    ],
    "Landroid/nfc/tech/NfcF;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","get","(Landroid/nfc/Tag;)"),
        ("F","transceive","([B)"),
    ],
    "Landroid/content/Context;" : [
        ("C","NFC_SERVICE","Ljava/lang/String;"),
    ],
    "Landroid/nfc/Tag;" : [
        ("F","getTechList","()"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("C","FEATURE_NFC","Ljava/lang/String;"),
    ],
    "Landroid/nfc/tech/MifareUltralight;" : [
        ("F","close","()"),
        ("F","connect","()"),
        ("F","readPages","(I)"),
        ("F","transceive","([B)"),
        ("F","writePage","(I [B)"),
    ],
    "Landroid/nfc/NfcManager;" : [
        ("F","getDefaultAdapter","()"),
    ],
    "Landroid/preference/PreferenceActivity;" : [
        ("C","SampleCode","Ljava/lang/String;"),
    ],
},

"android.permission.WRITE_CONTACTS" : {
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;" : [
        ("F","updateAdnRecordsInEfByIndex","(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","updateAdnRecordsInEfBySearch","(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;" : [
        ("F","updateAdnRecordsInEfByIndex","(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","updateAdnRecordsInEfBySearch","(I Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/content/Intent;" : [
        ("C","com.android.contacts.VIEW_NOTIFICATION","null"),
    ],
    "Landroid/pim/vcard/VCardEntry;" : [
        ("F","pushIntoContentResolver","(Landroid/content/ContentResolver;)"),
    ],
    "Landroid/provider/Contacts$Settings;" : [
        ("F","setSetting","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/pim/vcard/VCardEntryHandler;" : [
        ("F","onEntryCreated","(Landroid/pim/vcard/VCardEntry;)"),
    ],
    "Landroid/provider/Contacts$People;" : [
        ("F","addToGroup","(Landroid/content/ContentResolver; J J)"),
    ],
    "Landroid/pim/vcard/VCardEntryCommitter;" : [
        ("F","onEntryCreated","(Landroid/pim/vcard/VCardEntry;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://com.android.contacts"),
        ("F","update","content://com.android.contacts"),
        ("F","delete","content://com.android.contacts"),
        ("F","insert","content://contacts"),
        ("F","update","content://contacts"),
        ("F","delete","content://contacts"),
        ("F","insert","content://icc"),
        ("F","update","content://icc"),
        ("F","delete","content://icc"),
        ("F","insert","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_MAX_DIMENSIONS_URI"),
        ("F","update","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_MAX_DIMENSIONS_URI"),
        ("F","delete","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_MAX_DIMENSIONS_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Profile;->CONTENT_VCARD_URI"),
        ("F","update","Landroid/provider/ContactsContract$Profile;->CONTENT_VCARD_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Profile;->CONTENT_VCARD_URI"),
        ("F","insert","Landroid/provider/Contacts$Photos;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Photos;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Photos;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$StatusUpdates;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$StatusUpdates;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$StatusUpdates;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_VCARD_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_VCARD_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_VCARD_URI"),
        ("F","insert","Landroid/provider/ContactsContract$DeletedContacts;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$DeletedContacts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$DeletedContacts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$SyncState;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$SyncState;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$SyncState;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$Presence;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Presence;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Presence;->CONTENT_URI"),
        ("F","insert","Lcom/android/common/contacts/BaseEmailAddressAdapter$DirectoryListQuery;->URI"),
        ("F","update","Lcom/android/common/contacts/BaseEmailAddressAdapter$DirectoryListQuery;->URI"),
        ("F","delete","Lcom/android/common/contacts/BaseEmailAddressAdapter$DirectoryListQuery;->URI"),
        ("F","insert","Landroid/provider/ContactsContract$ProviderStatus;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$ProviderStatus;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$ProviderStatus;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_FILTER_URI"),
        ("F","insert","Lcom/android/common/contacts/DataUsageStatUpdater$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","update","Lcom/android/common/contacts/DataUsageStatUpdater$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","delete","Lcom/android/common/contacts/DataUsageStatUpdater$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","insert","Landroid/provider/Contacts$GroupMembership;->RAW_CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$GroupMembership;->RAW_CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$GroupMembership;->RAW_CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$Groups;->DELETED_CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Groups;->DELETED_CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Groups;->DELETED_CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/Contacts$People;->DELETED_CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$People;->DELETED_CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$People;->DELETED_CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Profile;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Profile;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Profile;->CONTENT_URI"),
        ("F","insert","Lcom/android/email/activity/setup/AccountSetupNames;->PROFILE_URI"),
        ("F","update","Lcom/android/email/activity/setup/AccountSetupNames;->PROFILE_URI"),
        ("F","delete","Lcom/android/email/activity/setup/AccountSetupNames;->PROFILE_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$StructuredPostal;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$StructuredPostal;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$StructuredPostal;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$AggregationExceptions;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$AggregationExceptions;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$AggregationExceptions;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_FREQUENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_FREQUENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_FREQUENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$RawContactsEntity;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$RawContactsEntity;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$RawContactsEntity;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$PhoneLookup;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$PhoneLookup;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$PhoneLookup;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/Contacts$Phones;->CONTENT_FILTER_URL"),
        ("F","update","Landroid/provider/Contacts$Phones;->CONTENT_FILTER_URL"),
        ("F","delete","Landroid/provider/Contacts$Phones;->CONTENT_FILTER_URL"),
        ("F","insert","Landroid/provider/Contacts$People;->WITH_EMAIL_OR_IM_FILTER_URI"),
        ("F","update","Landroid/provider/Contacts$People;->WITH_EMAIL_OR_IM_FILTER_URI"),
        ("F","delete","Landroid/provider/Contacts$People;->WITH_EMAIL_OR_IM_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$DataUsageFeedback;->DELETE_USAGE_URI"),
        ("F","update","Landroid/provider/ContactsContract$DataUsageFeedback;->DELETE_USAGE_URI"),
        ("F","delete","Landroid/provider/ContactsContract$DataUsageFeedback;->DELETE_USAGE_URI"),
        ("F","insert","Landroid/provider/ContactsContract$StreamItems;->CONTENT_PHOTO_URI"),
        ("F","update","Landroid/provider/ContactsContract$StreamItems;->CONTENT_PHOTO_URI"),
        ("F","delete","Landroid/provider/ContactsContract$StreamItems;->CONTENT_PHOTO_URI"),
        ("F","insert","Landroid/provider/Contacts$People;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$People;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$People;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$ContactMethods;->CONTENT_EMAIL_URI"),
        ("F","update","Landroid/provider/Contacts$ContactMethods;->CONTENT_EMAIL_URI"),
        ("F","delete","Landroid/provider/Contacts$ContactMethods;->CONTENT_EMAIL_URI"),
        ("F","insert","Landroid/provider/Contacts$Organizations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Organizations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Organizations;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$ProfileSyncState;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$ProfileSyncState;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$ProfileSyncState;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$ContactMethods;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$ContactMethods;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$ContactMethods;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_LOOKUP_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_LOOKUP_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_LOOKUP_URI"),
        ("F","insert","Landroid/provider/Contacts$Extensions;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Extensions;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Extensions;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Directory;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Directory;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Directory;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$GroupMembership;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$GroupMembership;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$GroupMembership;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_GROUP_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_GROUP_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_GROUP_URI"),
        ("F","insert","Lcom/android/ex/chips/BaseRecipientAdapter$DirectoryListQuery;->URI"),
        ("F","update","Lcom/android/ex/chips/BaseRecipientAdapter$DirectoryListQuery;->URI"),
        ("F","delete","Lcom/android/ex/chips/BaseRecipientAdapter$DirectoryListQuery;->URI"),
        ("F","insert","Landroid/provider/ContactsContract$Profile;->CONTENT_RAW_CONTACTS_URI"),
        ("F","update","Landroid/provider/ContactsContract$Profile;->CONTENT_RAW_CONTACTS_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Profile;->CONTENT_RAW_CONTACTS_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Data;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Data;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Data;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Groups;->CONTENT_SUMMARY_URI"),
        ("F","update","Landroid/provider/ContactsContract$Groups;->CONTENT_SUMMARY_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Groups;->CONTENT_SUMMARY_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract;->AUTHORITY_URI"),
        ("F","update","Landroid/provider/ContactsContract;->AUTHORITY_URI"),
        ("F","delete","Landroid/provider/ContactsContract;->AUTHORITY_URI"),
        ("F","insert","Landroid/provider/Contacts$Settings;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Settings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Settings;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$RawContactsEntity;->PROFILE_CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$RawContactsEntity;->PROFILE_CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$RawContactsEntity;->PROFILE_CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_MULTI_VCARD_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_MULTI_VCARD_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_MULTI_VCARD_URI"),
        ("F","insert","Landroid/provider/Contacts$Phones;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Phones;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Phones;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$Groups;->CONTENT_URI"),
        ("F","update","Landroid/provider/Contacts$Groups;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Contacts$Groups;->CONTENT_URI"),
        ("F","insert","Lcom/android/internal/notification/DemoContactNotificationScorer;->CONTACTS_URI"),
        ("F","update","Lcom/android/internal/notification/DemoContactNotificationScorer;->CONTACTS_URI"),
        ("F","delete","Lcom/android/internal/notification/DemoContactNotificationScorer;->CONTACTS_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Settings;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Settings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Settings;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","update","Landroid/provider/ContactsContract$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","delete","Landroid/provider/ContactsContract$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","insert","Landroid/provider/ContactsContract$StreamItems;->CONTENT_LIMIT_URI"),
        ("F","update","Landroid/provider/ContactsContract$StreamItems;->CONTENT_LIMIT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$StreamItems;->CONTENT_LIMIT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Groups;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Groups;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Groups;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$StatusUpdates;->PROFILE_CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$StatusUpdates;->PROFILE_CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$StatusUpdates;->PROFILE_CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_LOOKUP_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_LOOKUP_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_LOOKUP_URI"),
        ("F","insert","Landroid/provider/ContactsContract$RawContacts;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$RawContacts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$RawContacts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Contacts$People;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/Contacts$People;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/Contacts$People;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/ContactsContract$PinnedPositions;->UPDATE_URI"),
        ("F","update","Landroid/provider/ContactsContract$PinnedPositions;->UPDATE_URI"),
        ("F","delete","Landroid/provider/ContactsContract$PinnedPositions;->UPDATE_URI"),
        ("F","insert","Landroid/provider/ContactsContract$Contacts;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$Contacts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$Contacts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/ContactsContract$StreamItems;->CONTENT_URI"),
        ("F","update","Landroid/provider/ContactsContract$StreamItems;->CONTENT_URI"),
        ("F","delete","Landroid/provider/ContactsContract$StreamItems;->CONTENT_URI"),
    ],
    "Landroid/provider/CallLog$Calls;" : [
        ("F","removeExpiredEntries","(Landroid/content/Context;)"),
    ],
    "Landroid/provider/ContactsContract$Contacts;" : [
        ("F","markAsContacted","(Landroid/content/ContentResolver; J)"),
    ],
},

"android.permission.SEND_SMS" : {
    "Landroid/telephony/SmsManager;" : [
        ("F","getDefault","()"),
        ("F","sendDataMessage","(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendDataMessage","(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendMultipartTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)"),
        ("F","sendTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
    ],
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;" : [
        ("F","sendData","(Ljava/lang/String; Ljava/lang/String; I [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendMultipartText","(Ljava/lang/String; Ljava/lang/String; Ljava/util/List; Ljava/util/List; Ljava/util/List;)"),
        ("F","sendText","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
    ],
    "Landroid/telephony/gsm/SmsManager;" : [
        ("F","getDefault","()"),
        ("F","sendDataMessage","(Ljava/lang/String; Ljava/lang/String; S [B Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendDataMessage","(Ljava/lang/String; Ljava/lang/String; S [L; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
        ("F","sendMultipartTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/util/ArrayList; Ljava/util/ArrayList; Ljava/util/ArrayList;)"),
        ("F","sendTextMessage","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Landroid/app/PendingIntent; Landroid/app/PendingIntent;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
},

"com.android.browser.permission.WRITE_HISTORY_BOOKMARKS" : {
    "Landroid/provider/Browser;" : [
        ("C","BOOKMARKS_URI","Landroid/net/Uri;"),
        ("C","SEARCHES_URI","Landroid/net/Uri;"),
        ("F","addSearchUrl","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","clearHistory","(Landroid/content/ContentResolver;)"),
        ("F","clearSearches","(Landroid/content/ContentResolver;)"),
        ("F","deleteFromHistory","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","deleteHistoryTimeFrame","(Landroid/content/ContentResolver; J J)"),
        ("F","truncateHistory","(Landroid/content/ContentResolver;)"),
        ("F","updateVisitedHistory","(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
        ("F","clearSearches","(Landroid/content/ContentResolver;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://browser"),
        ("F","update","content://browser"),
        ("F","delete","content://browser"),
        ("F","insert","content://com.android.browser"),
        ("F","update","content://com.android.browser"),
        ("F","delete","content://com.android.browser"),
        ("F","insert","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","update","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","delete","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","insert","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","update","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","delete","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","update","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","delete","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","update","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","delete","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","insert","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Browser;->BOOKMARKS_URI"),
        ("F","update","Landroid/provider/Browser;->BOOKMARKS_URI"),
        ("F","delete","Landroid/provider/Browser;->BOOKMARKS_URI"),
    ],
},

"android.permission.AUTHENTICATE_ACCOUNTS" : {
    "Landroid/accounts/AccountManager;" : [
        ("F","addAccountExplicitly","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getPassword","(Landroid/accounts/Account;)"),
        ("F","getUserData","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","peekAuthToken","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setPassword","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setUserData","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","addAccountExplicitly","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getPassword","(Landroid/accounts/Account;)"),
        ("F","getUserData","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","peekAuthToken","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setPassword","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setUserData","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;" : [
        ("F","addAccount","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getPassword","(Landroid/accounts/Account;)"),
        ("F","getUserData","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","peekAuthToken","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setPassword","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setUserData","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/accounts/AccountManagerService;" : [
        ("F","addAccount","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","checkAuthenticateAccountsPermission","(Landroid/accounts/Account;)"),
        ("F","getPassword","(Landroid/accounts/Account;)"),
        ("F","getUserData","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","peekAuthToken","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setPassword","(Landroid/accounts/Account; Ljava/lang/String;)"),
        ("F","setUserData","(Landroid/accounts/Account; Ljava/lang/String; Ljava/lang/String;)"),
    ],
},

"android.permission.CLEAR_APP_USER_DATA" : {
    "Landroid/app/ActivityManager;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/app/ActivityManagerNative;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; LIPackageDataObserver;)"),
        ("F","clearApplicationUserData","(Ljava/lang/String; LIPackageDataObserver;)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","clearApplicationUserData","(Ljava/lang/String; LIPackageDataObserver;)"),
    ],
},

"ACCESS_DRM" : {
    "Landroid/provider/DrmStore;" : [
        ("F","enforceAccessDrmPermission","(Landroid/content/Context;)"),
    ],
},

"com.android.launcher.permission.INSTALL_SHORTCUT" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher.action.INSTALL_SHORTCUT","null"),
    ],
},

"android.permission.MANAGE_APP_TOKENS" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","addAppToken","(I Landroid/view/IApplicationToken; I I B)"),
        ("F","addWindowToken","(Landroid/os/IBinder; I)"),
        ("F","executeAppTransition","()"),
        ("F","moveAppToken","(I Landroid/os/IBinder;)"),
        ("F","moveAppTokensToBottom","(Ljava/util/List;)"),
        ("F","moveAppTokensToTop","(Ljava/util/List;)"),
        ("F","pauseKeyDispatching","(Landroid/os/IBinder;)"),
        ("F","prepareAppTransition","(I)"),
        ("F","removeAppToken","(Landroid/os/IBinder;)"),
        ("F","removeWindowToken","(Landroid/os/IBinder;)"),
        ("F","resumeKeyDispatching","(Landroid/os/IBinder;)"),
        ("F","setAppGroupId","(Landroid/os/IBinder; I)"),
        ("F","setAppOrientation","(Landroid/view/IApplicationToken; I)"),
        ("F","setAppStartingWindow","(Landroid/os/IBinder; Ljava/lang/String; I Ljava/lang/CharSequence; I I Landroid/os/IBinder; B)"),
        ("F","setAppVisibility","(Landroid/os/IBinder; B)"),
        ("F","setAppWillBeHidden","(Landroid/os/IBinder;)"),
        ("F","setEventDispatching","(B)"),
        ("F","setFocusedApp","(Landroid/os/IBinder; B)"),
        ("F","setNewConfiguration","(Landroid/content/res/Configuration;)"),
        ("F","startAppFreezingScreen","(Landroid/os/IBinder; I)"),
        ("F","stopAppFreezingScreen","(Landroid/os/IBinder; B)"),
        ("F","updateOrientationFromAppTokens","(Landroid/content/res/Configuration; Landroid/os/IBinder;)"),
    ],
},

"android.permission.RECEIVE_BOOT_COMPLETED" : {
    "Landroid/content/Intent;" : [
        ("C","ACTION_BOOT_COMPLETED","Ljava/lang/String;"),
    ],
},

"android.permission.WRITE_SMS" : {
    "Landroid/provider/Telephony$Sms$Outbox;" : [
        ("F","addMessage","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B J)"),
    ],
    "Landroid/provider/Telephony$Sms;" : [
        ("F","addMessageToUri","(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B J)"),
        ("F","addMessageToUri","(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B B)"),
        ("F","moveMessageToFolder","(Landroid/content/Context; Landroid/net/Uri; I I)"),
    ],
    "Landroid/provider/Telephony$Sms$Draft;" : [
        ("F","saveMessage","(Landroid/content/ContentResolver; Landroid/net/Uri; Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://mms-sms"),
        ("F","update","content://mms-sms"),
        ("F","delete","content://mms-sms"),
        ("F","insert","content://mms"),
        ("F","update","content://mms"),
        ("F","delete","content://mms"),
        ("F","insert","content://sms"),
        ("F","update","content://sms"),
        ("F","delete","content://sms"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_LOCKED_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_LOCKED_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_LOCKED_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Threads;->OBSOLETE_THREADS_URI"),
        ("F","update","Landroid/provider/Telephony$Threads;->OBSOLETE_THREADS_URI"),
        ("F","delete","Landroid/provider/Telephony$Threads;->OBSOLETE_THREADS_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->SEARCH_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->SEARCH_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->SEARCH_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Threads;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Threads;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Threads;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Threads;->THREAD_ID_CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Threads;->THREAD_ID_CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Threads;->THREAD_ID_CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms$Rate;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms$Rate;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms$Rate;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_CONVERSATIONS_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_CONVERSATIONS_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_CONVERSATIONS_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms;->REPORT_STATUS_URI"),
        ("F","update","Landroid/provider/Telephony$Mms;->REPORT_STATUS_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms;->REPORT_STATUS_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_UNDELIVERED_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_UNDELIVERED_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_UNDELIVERED_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms$Sent;->CONTENT_URI"),
        ("F","insert","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","insert","Landroid/provider/Telephony$Mms;->REPORT_REQUEST_URI"),
        ("F","update","Landroid/provider/Telephony$Mms;->REPORT_REQUEST_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms;->REPORT_REQUEST_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_DRAFT_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_DRAFT_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_DRAFT_URI"),
        ("F","insert","Landroid/provider/Telephony$Mms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","insert","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","insert","Landroid/provider/Telephony$Mms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Mms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Mms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms$PendingMessages;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms$PendingMessages;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms$PendingMessages;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$MmsSms;->CONTENT_FILTER_BYPHONE_URI"),
        ("F","update","Landroid/provider/Telephony$MmsSms;->CONTENT_FILTER_BYPHONE_URI"),
        ("F","delete","Landroid/provider/Telephony$MmsSms;->CONTENT_FILTER_BYPHONE_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
},

"ASEC_RENAME" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","renameSecureContainer","(Ljava/lang/String; Ljava/lang/String;)"),
    ],
},

"android.permission.WRITE_CALL_LOG" : {
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://call_log"),
        ("F","update","content://call_log"),
        ("F","delete","content://call_log"),
        ("F","insert","Landroid/provider/CallLog$Calls;->CONTENT_FILTER_URI"),
        ("F","update","Landroid/provider/CallLog$Calls;->CONTENT_FILTER_URI"),
        ("F","delete","Landroid/provider/CallLog$Calls;->CONTENT_FILTER_URI"),
        ("F","insert","Landroid/provider/CallLog;->CONTENT_URI"),
        ("F","update","Landroid/provider/CallLog;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CallLog;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CallLog$Calls;->CONTENT_URI"),
        ("F","update","Landroid/provider/CallLog$Calls;->CONTENT_URI"),
        ("F","delete","Landroid/provider/CallLog$Calls;->CONTENT_URI"),
        ("F","insert","Landroid/provider/CallLog$Calls;->CONTENT_URI_WITH_VOICEMAIL"),
        ("F","update","Landroid/provider/CallLog$Calls;->CONTENT_URI_WITH_VOICEMAIL"),
        ("F","delete","Landroid/provider/CallLog$Calls;->CONTENT_URI_WITH_VOICEMAIL"),
    ],
},

"android.permission.CHANGE_WIFI_MULTICAST_STATE" : {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;" : [
        ("F","acquireMulticastLock","(Landroid/os/IBinder; Ljava/lang/String;)"),
        ("F","initializeMulticastFiltering","()"),
        ("F","releaseMulticastLock","()"),
    ],
    "Landroid/net/wifi/WifiManager$MulticastLock;" : [
        ("F","acquire","()"),
        ("F","finalize","()"),
        ("F","release","()"),
    ],
    "Landroid/net/wifi/WifiManager;" : [
        ("F","initializeMulticastFiltering","()"),
    ],
},

"com.android.launcher3.permission.UNINSTALL_SHORTCUT" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher3.action.UNINSTALL_SHORTCUT","null"),
    ],
},

"android.permission.DELETE_PACKAGES" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","deletePackage","(Ljava/lang/String; LIPackageDeleteObserver; I)"),
        ("F","deletePackage","(Ljava/lang/String; LIPackageDeleteObserver; I)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","deletePackage","(Ljava/lang/String; LIPackageDeleteObserver; I)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","deletePackage","(Ljava/lang/String; Landroid/content/pm/IPackageDeleteObserver; I)"),
    ],
},

"android.permission.RECORD_AUDIO" : {
    "Landroid/media/AudioRecord;" : [
        ("F","<init>","(I I I I I)"),
    ],
    "Landroid/net/sip/SipAudioCall;" : [
        ("F","startAudio","()"),
    ],
    "Landroid/media/MediaRecorder;" : [
        ("F","setAudioSource","(I)"),
    ],
    "Landroid/speech/SpeechRecognizer;" : [
        ("F","cancel","()"),
        ("F","handleCancelMessage","()"),
        ("F","handleStartListening","(Landroid/content/Intent;)"),
        ("F","handleStopMessage","()"),
        ("F","startListening","(Landroid/content/Intent;)"),
        ("F","stopListening","()"),
    ],
},

"android.permission.MODIFY_AUDIO_SETTINGS" : {
    "Landroid/media/IAudioService$Stub$Proxy;" : [
        ("F","setBluetoothScoOn","(B)"),
        ("F","setMode","(I Landroid/os/IBinder;)"),
        ("F","setSpeakerphoneOn","(B)"),
        ("F","startBluetoothSco","(Landroid/os/IBinder;)"),
        ("F","stopBluetoothSco","(Landroid/os/IBinder;)"),
    ],
    "Landroid/net/sip/SipAudioCall;" : [
        ("F","setSpeakerMode","(B)"),
    ],
    "Landroid/media/AudioService;" : [
        ("F","setBluetoothScoOn","(B)"),
        ("F","setMode","(I Landroid/os/IBinder;)"),
        ("F","setSpeakerphoneOn","(B)"),
        ("F","startBluetoothSco","(Landroid/os/IBinder;)"),
        ("F","stopBluetoothSco","(Landroid/os/IBinder;)"),
    ],
    "Landroid/server/BluetoothA2dpService;" : [
        ("F","checkSinkSuspendState","(I)"),
        ("F","handleSinkStateChange","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","onBluetoothDisable","()"),
        ("F","onBluetoothEnable","()"),
    ],
    "Landroid/media/AudioManager;" : [
        ("F","startBluetoothSco","()"),
        ("F","stopBluetoothSco","()"),
        ("F","isBluetoothA2dpOn","()"),
        ("F","isWiredHeadsetOn","()"),
        ("F","setBluetoothScoOn","(B)"),
        ("F","setMicrophoneMute","(B)"),
        ("F","setMode","(I)"),
        ("F","setParameter","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setParameters","(Ljava/lang/String;)"),
        ("F","setSpeakerphoneOn","(B)"),
        ("F","startBluetoothSco","()"),
        ("F","stopBluetoothSco","()"),
    ],
},

"android.permission.SEND_RESPOND_VIA_MESSAGE" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.RESPOND_VIA_MESSAGE","null"),
    ],
},

"android.permission.BIND_INPUT_METHOD" : {
    "Landroid/view/inputmethod/InputMethod;" : [
        ("C","SERVICE_INTERFACE","Ljava/lang/String;"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.view.InputMethod","null"),
    ],
},

"android.permission.SET_TIME_ZONE" : {
    "Landroid/app/IAlarmManager$Stub$Proxy;" : [
        ("F","setTimeZone","(Ljava/lang/String;)"),
    ],
    "Landroid/app/AlarmManager;" : [
        ("F","setTimeZone","(Ljava/lang/String;)"),
        ("F","setTimeZone","(Ljava/lang/String;)"),
    ],
},

"android.permission.DUMP" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.BUGREPORT_FINISHED","null"),
    ],
    "Lcom/android/server/WallpaperManagerService;" : [
        ("F","dump","(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Stri;)"),
    ],
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","isViewServerRunning","()"),
        ("F","startViewServer","(I)"),
        ("F","stopViewServer","()"),
    ],
    "Landroid/os/IBinder;" : [
        ("C","DUMP_TRANSACTION","I"),
    ],
    "Landroid/os/Debug;" : [
        ("F","dumpService","(Ljava/lang/String; Ljava/io/FileDescriptor; [Ljava/lang/String;)"),
    ],
    "Landroid/content/ContentService;" : [
        ("F","dump","(Ljava/io/FileDescriptor; Ljava/io/PrintWriter; [L[Ljava/lang/Strin;)"),
    ],
},

"android.permission.SET_TIME" : {
    "Landroid/app/IAlarmManager$Stub$Proxy;" : [
        ("F","setTime","(J)"),
    ],
    "Landroid/app/AlarmManager;" : [
        ("F","setTime","(J)"),
        ("F","setTimeZone","(Ljava/lang/String;)"),
        ("F","setTime","(J)"),
    ],
},

"com.android.email.permission.ACCESS_PROVIDER" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.email.ACCOUNT_INTENT","null"),
        ("C","com.android.email.IMAP_INTENT","null"),
        ("C","com.android.email.POLICY_INTENT","null"),
        ("C","com.android.email.POP3_INTENT","null"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.email.notifier"),
        ("F","insert","content://com.android.email.notifier"),
        ("F","update","content://com.android.email.notifier"),
        ("F","delete","content://com.android.email.notifier"),
        ("F","query","content://com.android.email.provider"),
        ("F","insert","content://com.android.email.provider"),
        ("F","update","content://com.android.email.provider"),
        ("F","delete","content://com.android.email.provider"),
    ],
},

"android.app.cts.permission.TEST_GRANTED" : {
    "Landroid/content/Intent;" : [
        ("C","android.app.cts.activity.SERVICE_LOCAL_GRANTED","null"),
    ],
},

"com.android.gallery3d.permission.GALLERY_PROVIDER" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.gallery3d.provider"),
        ("F","insert","content://com.android.gallery3d.provider"),
        ("F","update","content://com.android.gallery3d.provider"),
        ("F","delete","content://com.android.gallery3d.provider"),
        ("F","query","Lcom/android/gallery3d/provider/GalleryProvider;->BASE_URI"),
        ("F","insert","Lcom/android/gallery3d/provider/GalleryProvider;->BASE_URI"),
        ("F","update","Lcom/android/gallery3d/provider/GalleryProvider;->BASE_URI"),
        ("F","delete","Lcom/android/gallery3d/provider/GalleryProvider;->BASE_URI"),
    ],
},

"com.android.permission.WHITELIST_BLUETOOTH_DEVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.btopp.intent.action.HANDOVER_SEND","*/*"),
        ("C","android.btopp.intent.action.HANDOVER_SEND_MULTIPLE","*/*"),
        ("C","android.btopp.intent.action.WHITELIST_DEVICE android.btopp.intent.action.STOP_HANDOVER_TRANSFER","null"),
    ],
},

"ACCESS_DOWNLOAD_MANAGER" : {
    "Landroid/net/Downloads$ById;" : [
        ("F","deleteDownload","(Landroid/content/Context; J)"),
        ("F","getMimeTypeForId","(Landroid/content/Context; J)"),
        ("F","getStatus","(Landroid/content/Context; J)"),
        ("F","openDownload","(Landroid/content/Context; J Ljava/lang/String;)"),
        ("F","openDownloadStream","(Landroid/content/Context; J)"),
        ("F","startDownloadByUri","(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/net/Downloads$DownloadBase;" : [
        ("F","startDownloadByUri","(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/net/Downloads$ByUri;" : [
        ("F","getCurrentOtaDownloads","(Landroid/content/Context; Ljava/lang/String;)"),
        ("F","getProgressCursor","(Landroid/content/Context; J)"),
        ("F","getStatus","(Landroid/content/Context; Ljava/lang/String; J)"),
        ("F","removeAllDownloadsByPackage","(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","startDownloadByUri","(Landroid/content/Context; Ljava/lang/String; Ljava/lang/String; B I B B Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
    ],
},

"android.permission.READ_CELL_BROADCASTS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://cellbroadcasts"),
        ("F","query","Landroid/provider/Telephony$CellBroadcasts;->CONTENT_URI"),
    ],
},

"android.permission.BIND_DEVICE_ADMIN" : {
    "Landroid/app/admin/DeviceAdminReceiver;" : [
        ("C","ACTION_DEVICE_ADMIN_ENABLED","Ljava/lang/String;"),
    ],
    "Landroid/app/admin/IDevicePolicyManager$Stub$Proxy;" : [
        ("F","getRemoveWarning","(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
        ("F","reportFailedPasswordAttempt","()"),
        ("F","reportSuccessfulPasswordAttempt","()"),
        ("F","setActiveAdmin","(Landroid/content/ComponentName;)"),
        ("F","setActivePasswordState","(I I)"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.app.action.DEVICE_ADMIN_DISABLED","null"),
        ("C","android.app.action.DEVICE_ADMIN_ENABLED","null"),
    ],
    "Landroid/app/admin/DevicePolicyManager;" : [
        ("F","getRemoveWarning","(Landroid/content/ComponentName; Landroid/os/RemoteCallback;)"),
        ("F","reportFailedPasswordAttempt","()"),
        ("F","reportSuccessfulPasswordAttempt","()"),
        ("F","setActiveAdmin","(Landroid/content/ComponentName;)"),
        ("F","setActivePasswordState","(I I)"),
    ],
},

"android.permission.CALL_PHONE" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.CALL","sip"),
        ("C","android.intent.action.CALL","tel"),
        ("C","android.intent.action.CALL","vnd.android.cursor.item/phone vnd.android.cursor.item/phone_v2 vnd.android.cursor.item/person"),
        ("C","android.intent.action.CALL","voicemail"),
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
        ("F","call","(Ljava/lang/String;)"),
        ("F","endCall","()"),
    ],
},

"android.permission.FLASHLIGHT" : {
    "Landroid/os/IHardwareService$Stub$Proxy;" : [
        ("F","setFlashlightEnabled","(B)"),
    ],
},

"android.permission.READ_PHONE_STATE" : {
    "Landroid/telephony/PhoneStateListener;" : [
        ("C","LISTEN_CALL_FORWARDING_INDICATOR","I"),
        ("C","LISTEN_CALL_STATE","I"),
        ("C","LISTEN_DATA_ACTIVITY","I"),
        ("C","LISTEN_MESSAGE_WAITING_INDICATOR","I"),
        ("C","LISTEN_SIGNAL_STRENGTH","I"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.cellbroadcastreceiver.GET_LATEST_CB_AREA_INFO","null"),
    ],
    "Lcom/android/internal/telephony/IPhoneSubInfo$Stub$Proxy;" : [
        ("F","getDeviceId","()"),
        ("F","getDeviceSvn","()"),
        ("F","getIccSerialNumber","()"),
        ("F","getLine1AlphaTag","()"),
        ("F","getLine1Number","()"),
        ("F","getSubscriberId","()"),
        ("F","getVoiceMailAlphaTag","()"),
        ("F","getVoiceMailNumber","()"),
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
        ("F","isSimPinEnabled","()"),
    ],
    "Landroid/telephony/TelephonyManager;" : [
        ("C","ACTION_PHONE_STATE_CHANGED","Ljava/lang/String;"),
        ("F","getDeviceId","()"),
        ("F","getDeviceSoftwareVersion","()"),
        ("F","getLine1Number","()"),
        ("F","getSimSerialNumber","()"),
        ("F","getSubscriberId","()"),
        ("F","getVoiceMailAlphaTag","()"),
        ("F","getVoiceMailNumber","()"),
        ("F","getDeviceId","()"),
        ("F","getDeviceSoftwareVersion","()"),
        ("F","getLine1AlphaTag","()"),
        ("F","getLine1Number","()"),
        ("F","getSimSerialNumber","()"),
        ("F","getSubscriberId","()"),
        ("F","getVoiceMailAlphaTag","()"),
        ("F","getVoiceMailNumber","()"),
        ("F","listen","(Landroid/telephony/PhoneStateListener; I)"),
    ],
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;" : [
        ("F","listen","(Ljava/lang/String; Lcom/android/internal/telephony/IPhoneStateListener; I B)"),
    ],
    "Landroid/telephony/PhoneNumberUtils;" : [
        ("F","isVoiceMailNumber","(Ljava/lang/String;)"),
    ],
    "Landroid/accounts/AccountManagerService$SimWatcher;" : [
        ("F","onReceive","(Landroid/content/Context; Landroid/content/Intent;)"),
    ],
    "Lcom/android/internal/telephony/CallerInfo;" : [
        ("F","markAsVoiceMail","()"),
    ],
    "Landroid/os/Build/VERSION_CODES;" : [
        ("C","DONUT","I"),
    ],
},

"com.android.frameworks.coretests.permission.TEST_DENIED" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.frameworks.coretests.activity.BROADCAST_LOCAL_DENIED","null"),
        ("C","com.android.frameworks.coretests.activity.BROADCAST_REMOTE_DENIED","null"),
        ("C","com.android.frameworks.coretests.activity.SERVICE_LOCAL_DENIED","null"),
    ],
},

"android.permission.ACCESS_COARSE_LOCATION" : {
    "Landroid/telephony/TelephonyManager;" : [
        ("F","getCellLocation","()"),
    ],
    "Landroid/location/LocationManager;" : [
        ("C","NETWORK_PROVIDER","Ljava/lang/String;"),
    ],
    "Landroid/telephony/PhoneStateListener;" : [
        ("C","LISTEN_CELL_LOCATION","I"),
    ],
},

"android.permission.WRITE_SECURE_SETTINGS" : {
    "Landroid/os/IPowerManager$Stub$Proxy;" : [
        ("F","setMaximumScreenOffTimeount","(I)"),
    ],
    "Landroid/content/Intent;" : [
        ("C","com.android.location.service.FusedLocationProvider","null"),
    ],
    "Landroid/server/BluetoothService;" : [
        ("F","setScanMode","(I I)"),
    ],
    "Landroid/bluetooth/BluetoothAdapter;" : [
        ("F","setScanMode","(I I)"),
        ("F","setScanMode","(I)"),
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;" : [
        ("F","setScanMode","(I I)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","setInstallLocation","(I)"),
    ],
},

"android.permission.UPDATE_DEVICE_STATS" : {
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;" : [
        ("F","notePauseComponent","(LComponentName;)"),
        ("F","noteResumeComponent","(LComponentName;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;" : [
        ("F","noteFullWifiLockAcquired","(I)"),
        ("F","noteFullWifiLockReleased","(I)"),
        ("F","noteInputEvent","()"),
        ("F","notePhoneDataConnectionState","(I B)"),
        ("F","notePhoneOff","()"),
        ("F","notePhoneOn","()"),
        ("F","notePhoneSignalStrength","(LSignalStrength;)"),
        ("F","notePhoneState","(I)"),
        ("F","noteScanWifiLockAcquired","(I)"),
        ("F","noteScanWifiLockReleased","(I)"),
        ("F","noteScreenBrightness","(I)"),
        ("F","noteScreenOff","()"),
        ("F","noteScreenOn","()"),
        ("F","noteStartGps","(I)"),
        ("F","noteStartSensor","(I I)"),
        ("F","noteStartWakelock","(I Ljava/lang/String; I)"),
        ("F","noteStopGps","(I)"),
        ("F","noteStopSensor","(I I)"),
        ("F","noteStopWakelock","(I Ljava/lang/String; I)"),
        ("F","noteUserActivity","(I I)"),
        ("F","noteWifiMulticastDisabled","(I)"),
        ("F","noteWifiMulticastEnabled","(I)"),
        ("F","noteWifiOff","(I)"),
        ("F","noteWifiOn","(I)"),
        ("F","noteWifiRunning","()"),
        ("F","noteWifiStopped","()"),
        ("F","recordCurrentLevel","(I)"),
        ("F","setOnBattery","(B I)"),
    ],
},

"android.permission.MANAGE_DOCUMENTS" : {
    "Landroid/content/Intent;" : [
        ("C","android.provider.action.MANAGE_DOCUMENT","null"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.externalstorage.documents"),
        ("F","insert","content://com.android.externalstorage.documents"),
        ("F","update","content://com.android.externalstorage.documents"),
        ("F","delete","content://com.android.externalstorage.documents"),
        ("F","query","content://com.android.providers.downloads.documents"),
        ("F","insert","content://com.android.providers.downloads.documents"),
        ("F","update","content://com.android.providers.downloads.documents"),
        ("F","delete","content://com.android.providers.downloads.documents"),
        ("F","query","content://com.android.providers.media.documents"),
        ("F","insert","content://com.android.providers.media.documents"),
        ("F","update","content://com.android.providers.media.documents"),
        ("F","delete","content://com.android.providers.media.documents"),
        ("F","query","content://com.example.documents"),
        ("F","insert","content://com.example.documents"),
        ("F","update","content://com.example.documents"),
        ("F","delete","content://com.example.documents"),
    ],
},

"CHANGE_BACKGROUND_DATA_SETTING" : {
    "Landroid/net/ConnectivityManager;" : [
        ("F","setBackgroundDataSetting","(B)"),
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;" : [
        ("F","setBackgroundDataSetting","(B)"),
    ],
},

"android.permission.SYSTEM_ALERT_WINDOW" : {
    "Landroid/view/IWindowSession$Stub$Proxy;" : [
        ("F","add","(Landroid/view/IWindow; Landroid/view/WindowManager$LayoutParams; I Landroid/graphics/Rect;)"),
    ],
},

"UPDATE_DEVICE_STATS			" : {
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;" : [
        ("F","noteLaunchTime","(LComponentName;)"),
    ],
},

"android.permission.BROADCAST_SMS" : {
    "Landroid/content/Intent;" : [
        ("C","android.provider.Telephony.SMS_CB_RECEIVED","null"),
        ("C","android.provider.Telephony.SMS_DELIVER","null"),
        ("C","android.provider.Telephony.SMS_EMERGENCY_CB_RECEIVED","null"),
        ("C","android.provider.Telephony.SMS_SERVICE_CATEGORY_PROGRAM_DATA_RECEIVED","null"),
    ],
},

"CHANGE_WIMAX_STATE" : {
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;" : [
        ("F","setWimaxEnable","()"),
    ],
},

"android.permission.GET_TASKS" : {
    "Landroid/app/ActivityManager;" : [
        ("F","getRecentTasks","(I I)"),
        ("F","getRunningTasks","(I)"),
        ("F","getRecentTasks","(I I)"),
        ("F","getRunningTasks","(I)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","getRecentTasks","(I I)"),
        ("F","getTasks","(I I Landroid/app/IThumbnailReceiver;)"),
    ],
    "Landroid/app/ActivityManagerNative;" : [
        ("F","getRecentTasks","(I I)"),
        ("F","getRunningTasks","(I)"),
    ],
},

"MOVE_PACKAGE" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","movePackage","(Ljava/lang/String; LIPackageMoveObserver; I)"),
        ("F","movePackage","(Ljava/lang/String; LIPackageMoveObserver; I)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","movePackage","(Ljava/lang/String; LIPackageMoveObserver; I)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","movePackage","(Ljava/lang/String; Landroid/content/pm/IPackageMoveObserver; I)"),
    ],
},

"android.permission.WAKE_LOCK" : {
    "Landroid/net/wifi/WifiManager$WifiLock;" : [
        ("F","acquire","()"),
        ("F","finalize","()"),
        ("F","release","()"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
    "Landroid/os/IPowerManager$Stub$Proxy;" : [
        ("F","acquireWakeLock","(I Landroid/os/IBinder; Ljava/lang/String;)"),
        ("F","releaseWakeLock","(Landroid/os/IBinder; I)"),
    ],
    "Landroid/os/PowerManager$WakeLock;" : [
        ("F","acquire","()"),
        ("F","acquire","(J)"),
        ("F","release","()"),
        ("F","release","(I)"),
    ],
    "Landroid/bluetooth/ScoSocket;" : [
        ("F","acquireWakeLock","()"),
        ("F","close","()"),
        ("F","finalize","()"),
        ("F","releaseWakeLock","()"),
        ("F","releaseWakeLockNow","()"),
    ],
    "Landroid/net/sip/SipAudioCall;" : [
        ("F","startAudio","()"),
    ],
    "Landroid/os/PowerManager;" : [
        ("C","ACQUIRE_CAUSES_WAKEUP","I"),
        ("C","FULL_WAKE_LOCK","I"),
        ("C","ON_AFTER_RELEASE","I"),
        ("C","PARTIAL_WAKE_LOCK","I"),
        ("C","SCREEN_BRIGHT_WAKE_LOCK","I"),
        ("C","SCREEN_DIM_WAKE_LOCK","I"),
        ("F","newWakeLock","(I Ljava/lang/String;)"),
    ],
    "Landroid/media/MediaPlayer;" : [
        ("F","setWakeMode","(Landroid/content/Context; I)"),
        ("F","start","()"),
        ("F","stayAwake","(B)"),
        ("F","stop","()"),
    ],
    "Landroid/media/AsyncPlayer;" : [
        ("F","acquireWakeLock","()"),
        ("F","enqueueLocked","(Landroid/media/AsyncPlayer$Command;)"),
        ("F","play","(Landroid/content/Context; Landroid/net/Uri; B I)"),
        ("F","releaseWakeLock","()"),
        ("F","stop","()"),
    ],
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;" : [
        ("F","acquireWifiLock","(Landroid/os/IBinder; I Ljava/lang/String;)"),
        ("F","releaseWifiLock","(Landroid/os/IBinder;)"),
    ],
    "Landroid/bluetooth/HeadsetBase;" : [
        ("F","acquireWakeLock","()"),
        ("F","finalize","()"),
        ("F","handleInput","(Ljava/lang/String;)"),
        ("F","releaseWakeLock","()"),
    ],
},

"ACCESS_WIMAX_STATE" : {
    "Lcom/htc/net/wimax/WimaxController$Stub$Proxy;" : [
        ("F","getConnectionInf","()"),
        ("F","getWimaxStat","()"),
        ("F","isBackoffStat","()"),
        ("F","isWimaxEnable","()"),
    ],
},

"com.android.launcher3.permission.WRITE_SETTINGS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://com.android.launcher3.settings"),
        ("F","update","content://com.android.launcher3.settings"),
        ("F","delete","content://com.android.launcher3.settings"),
    ],
},

"android.permission.CHANGE_WIFI_STATE" : {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;" : [
        ("F","addOrUpdateNetwork","(Landroid/net/wifi/WifiConfiguration;)"),
        ("F","disableNetwork","(I)"),
        ("F","disconnect","()"),
        ("F","enableNetwork","(I B)"),
        ("F","pingSupplicant","()"),
        ("F","reassociate","()"),
        ("F","reconnect","()"),
        ("F","removeNetwork","(I)"),
        ("F","saveConfiguration","()"),
        ("F","setNumAllowedChannels","(I B)"),
        ("F","setWifiApEnabled","(Landroid/net/wifi/WifiConfiguration; B)"),
        ("F","setWifiEnabled","(B)"),
        ("F","startScan","(B)"),
    ],
    "Landroid/net/wifi/WifiManager;" : [
        ("F","addNetwork","(Landroid/net/wifi/WifiConfiguration;)"),
        ("F","addOrUpdateNetwork","(Landroid/net/wifi/WifiConfiguration;)"),
        ("F","disableNetwork","(I)"),
        ("F","disconnect","()"),
        ("F","enableNetwork","(I B)"),
        ("F","pingSupplicant","()"),
        ("F","reassociate","()"),
        ("F","reconnect","()"),
        ("F","removeNetwork","(I)"),
        ("F","saveConfiguration","()"),
        ("F","setNumAllowedChannels","(I B)"),
        ("F","setWifiApEnabled","(Landroid/net/wifi/WifiConfiguration; B)"),
        ("F","setWifiEnabled","(B)"),
        ("F","startScan","()"),
        ("F","startScanActive","()"),
    ],
},

"android.permission.RECEIVE_SMS" : {
    "Landroid/telephony/SmsManager;" : [
        ("F","copyMessageToIcc","([L; [L; I)"),
        ("F","deleteMessageFromIcc","(I)"),
        ("F","getAllMessagesFromIcc","()"),
        ("F","updateMessageOnIcc","(I I [L;)"),
    ],
    "Lcom/android/internal/telephony/ISms$Stub$Proxy;" : [
        ("F","copyMessageToIccEf","(I [B [B)"),
        ("F","getAllMessagesFromIccEf","()"),
        ("F","updateMessageOnIccEf","(I I [B)"),
    ],
    "Landroid/telephony/gsm/SmsManager;" : [
        ("F","copyMessageToSim","([L; [L; I)"),
        ("F","deleteMessageFromSim","(I)"),
        ("F","getAllMessagesFromSim","()"),
        ("F","updateMessageOnSim","(I I [L;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","insert","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","update","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","delete","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","insert","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","update","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","delete","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","update","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
},

"android.permission.READ_CONTACTS" : {
    "Lcom/android/internal/telephony/IccPhoneBookInterfaceManager$Stub$Proxy;" : [
        ("F","getAdnRecordsInEf","(I)"),
    ],
    "Landroid/provider/ContactsContract$Data;" : [
        ("F","getContactLookupUri","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
    ],
    "Landroid/pim/vcard/VCardComposer$OneEntryHandler;" : [
        ("F","onInit","(Landroid/content/Context;)"),
    ],
    "Lcom/android/internal/telephony/CallerInfo;" : [
        ("F","getCallerId","(Landroid/content/Context; Ljava/lang/String;)"),
        ("F","getCallerInfo","(Landroid/content/Context; Ljava/lang/String;)"),
    ],
    "Landroid/provider/Contacts$Settings;" : [
        ("F","getSetting","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"),
    ],
    "Landroid/widget/QuickContactBadge;" : [
        ("F","assignContactFromEmail","(Ljava/lang/String; B)"),
        ("F","assignContactFromPhone","(Ljava/lang/String; B)"),
        ("F","trigger","(Landroid/net/Uri;)"),
    ],
    "Landroid/provider/ContactsContract$RawContacts;" : [
        ("F","getContactLookupUri","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
    ],
    "Landroid/provider/ContactsContract$Contacts;" : [
        ("F","getLookupUri","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ("F","lookupContact","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ("F","openContactPhotoInputStream","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","openFileDescriptor","(Landroid/net/Uri; Ljava/lang/String;)"),
        ("F","openInputStream","(Landroid/net/Uri;)"),
        ("F","openOutputStream","(Landroid/net/Uri;)"),
        ("F","query","(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"),
        ("F","query","content://com.android.contacts"),
        ("F","query","content://com.android.exchange.directory.provider"),
        ("F","query","content://contacts"),
        ("F","query","content://icc"),
        ("F","query","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_MAX_DIMENSIONS_URI"),
        ("F","query","Landroid/provider/ContactsContract$Profile;->CONTENT_VCARD_URI"),
        ("F","query","Landroid/provider/Contacts$Photos;->CONTENT_URI"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/ContactsContract$StatusUpdates;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_VCARD_URI"),
        ("F","query","Landroid/provider/ContactsContract$DeletedContacts;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$SyncState;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$Presence;->CONTENT_URI"),
        ("F","query","Lcom/android/common/contacts/BaseEmailAddressAdapter$DirectoryListQuery;->URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Lcom/android/common/contacts/DataUsageStatUpdater$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_FILTER_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Landroid/provider/Contacts$GroupMembership;->RAW_CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$Groups;->DELETED_CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$People;->DELETED_CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$Profile;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$StructuredPostal;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$AggregationExceptions;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_FREQUENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Callable;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$RawContactsEntity;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Contactables;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Landroid/provider/Contacts$Phones;->CONTENT_FILTER_URL"),
        ("F","query","Landroid/provider/Contacts$People;->WITH_EMAIL_OR_IM_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_STREQUENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$DataUsageFeedback;->DELETE_USAGE_URI"),
        ("F","query","Landroid/provider/ContactsContract$StreamItems;->CONTENT_PHOTO_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Contacts$People;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$ContactMethods;->CONTENT_EMAIL_URI"),
        ("F","query","Landroid/provider/Contacts$Organizations;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$ProfileSyncState;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$ContactMethods;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_LOOKUP_URI"),
        ("F","query","Landroid/provider/Contacts$Extensions;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Directory;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$GroupMembership;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$PhoneLookup;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_GROUP_URI"),
        ("F","query","Lcom/android/ex/chips/BaseRecipientAdapter$DirectoryListQuery;->URI"),
        ("F","query","Landroid/provider/ContactsContract$Profile;->CONTENT_RAW_CONTACTS_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Email;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$DisplayPhoto;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$Data;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Groups;->CONTENT_SUMMARY_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract;->AUTHORITY_URI"),
        ("F","query","Lcom/android/email/activity/setup/AccountSetupNames;->PROFILE_URI"),
        ("F","query","Landroid/provider/ContactsContract$ProviderStatus;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$Settings;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$RawContactsEntity;->PROFILE_CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_MULTI_VCARD_URI"),
        ("F","query","Landroid/provider/Contacts$Phones;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$Groups;->CONTENT_URI"),
        ("F","query","Lcom/android/internal/notification/DemoContactNotificationScorer;->CONTACTS_URI"),
        ("F","query","Landroid/provider/ContactsContract$Settings;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$DataUsageFeedback;->FEEDBACK_URI"),
        ("F","query","Landroid/provider/ContactsContract$StreamItems;->CONTENT_LIMIT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Groups;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$StatusUpdates;->PROFILE_CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_LOOKUP_URI"),
        ("F","query","Landroid/provider/ContactsContract$RawContacts;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$CommonDataKinds$Phone;->CONTENT_URI"),
        ("F","query","Landroid/provider/Contacts$People;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/ContactsContract$PinnedPositions;->UPDATE_URI"),
        ("F","query","Landroid/provider/ContactsContract$Contacts;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
        ("F","query","Landroid/provider/ContactsContract$StreamItems;->CONTENT_URI"),
    ],
    "Landroid/app/ContextImpl$ApplicationContentResolver;" : [
        ("F","openFileDescriptor","(Landroid/net/Uri; Ljava/lang/String;)"),
        ("F","openInputStream","(Landroid/net/Uri;)"),
        ("F","openOutputStream","(Landroid/net/Uri;)"),
        ("F","query","(Landroid/net/Uri; [L[Ljava/lang/Strin; Ljava/lang/String; [L[Ljava/lang/Strin; Ljava/lang/String;)"),
    ],
    "Landroid/provider/CallLog$Calls;" : [
        ("F","addCall","(Lcom/android/internal/telephony/CallerInfo; Landroid/content/Context; Ljava/lang/String; I I J I)"),
        ("F","getLastOutgoingCall","(Landroid/content/Context;)"),
    ],
    "Landroid/provider/Contacts$People;" : [
        ("F","addToGroup","(Landroid/content/ContentResolver; J Ljava/lang/String;)"),
        ("F","addToMyContactsGroup","(Landroid/content/ContentResolver; J)"),
        ("F","createPersonInMyContactsGroup","(Landroid/content/ContentResolver; Landroid/content/ContentValues;)"),
        ("F","loadContactPhoto","(Landroid/content/Context; Landroid/net/Uri; I Landroid/graphics/BitmapFactory$Options;)"),
        ("F","markAsContacted","(Landroid/content/ContentResolver; J)"),
        ("F","openContactPhotoInputStream","(Landroid/content/ContentResolver; Landroid/net/Uri;)"),
        ("F","queryGroups","(Landroid/content/ContentResolver; J)"),
        ("F","setPhotoData","(Landroid/content/ContentResolver; Landroid/net/Uri; [L;)"),
        ("F","tryGetMyContactsGroupId","(Landroid/content/ContentResolver;)"),
    ],
    "Landroid/pim/vcard/VCardComposer$HandlerForOutputStream;" : [
        ("F","onInit","(Landroid/content/Context;)"),
    ],
    "Lcom/android/internal/telephony/IIccPhoneBook$Stub$Proxy;" : [
        ("F","getAdnRecordsInEf","(I)"),
    ],
    "Landroid/provider/ContactsContract$CommonDataKinds$Phone;" : [
        ("C","CONTENT_URI","Landroid/net/Uri;"),
    ],
    "Landroid/pim/vcard/VCardComposer;" : [
        ("F","createOneEntry","()"),
        ("F","createOneEntry","(Ljava/lang/reflect/Method;)"),
        ("F","createOneEntryInternal","(Ljava/lang/String; Ljava/lang/reflect/Method;)"),
        ("F","init","()"),
        ("F","init","(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
    ],
},

"com.android.cts.permissionNotUsedWithSignature" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://ctspermissionwithsignaturepath"),
        ("F","insert","content://ctspermissionwithsignaturepath"),
        ("F","update","content://ctspermissionwithsignaturepath"),
        ("F","delete","content://ctspermissionwithsignaturepath"),
    ],
},

"android.permission.BLUETOOTH" : {
    "Landroid/os/Process;" : [
        ("C","BLUETOOTH_GID","I"),
    ],
    "Landroid/bluetooth/BluetoothSocket;" : [
        ("F","connect","()"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.bluetooth.adapter.action.REQUEST_DISCOVERABLE android.bluetooth.adapter.action.REQUEST_ENABLE","null"),
    ],
    "Landroid/bluetooth/BluetoothAssignedNumbers;" : [
        ("C","BLUETOOTH_SIG","I"),
    ],
    "Landroid/provider/Settings;" : [
        ("C","ACTION_BLUETOOTH_SETTINGS","Ljava/lang/String;"),
    ],
    "Landroid/bluetooth/BluetoothHeadset;" : [
        ("C","ACTION_AUDIO_STATE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_CONNECTION_STATE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_VENDOR_SPECIFIC_HEADSET_EVENT","Ljava/lang/String;"),
        ("F","getConnectedDevices","()"),
        ("F","getConnectionState","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getDevicesMatchingConnectionStates","([I)"),
        ("F","isAudioConnected","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","startVoiceRecognition","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","stopVoiceRecognition","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getBatteryUsageHint","()"),
        ("F","getCurrentHeadset","()"),
        ("F","getPriority","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getState","()"),
        ("F","isConnected","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","startVoiceRecognition","()"),
        ("F","stopVoiceRecognition","()"),
    ],
    "Landroid/server/BluetoothService;" : [
        ("F","addRemoteDeviceProperties","(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ("F","addRfcommServiceRecord","(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)"),
        ("F","fetchRemoteUuids","(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)"),
        ("F","getAddress","()"),
        ("F","getAddressFromObjectPath","(Ljava/lang/String;)"),
        ("F","getAllProperties","()"),
        ("F","getBluetoothState","()"),
        ("F","getBondState","(Ljava/lang/String;)"),
        ("F","getDiscoverableTimeout","()"),
        ("F","getName","()"),
        ("F","getObjectPathFromAddress","(Ljava/lang/String;)"),
        ("F","getProperty","(Ljava/lang/String;)"),
        ("F","getPropertyInternal","(Ljava/lang/String;)"),
        ("F","getRemoteClass","(Ljava/lang/String;)"),
        ("F","getRemoteName","(Ljava/lang/String;)"),
        ("F","getRemoteServiceChannel","(Ljava/lang/String; Landroid/os/ParcelUuid;)"),
        ("F","getRemoteUuids","(Ljava/lang/String;)"),
        ("F","getScanMode","()"),
        ("F","getTrustState","(Ljava/lang/String;)"),
        ("F","isDiscovering","()"),
        ("F","isEnabled","()"),
        ("F","listBonds","()"),
        ("F","removeServiceRecord","(I)"),
        ("F","sendUuidIntent","(Ljava/lang/String;)"),
        ("F","setLinkTimeout","(Ljava/lang/String; I)"),
        ("F","setPropertyBoolean","(Ljava/lang/String; B)"),
        ("F","setPropertyInteger","(Ljava/lang/String; I)"),
        ("F","setPropertyString","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","updateDeviceServiceChannelCache","(Ljava/lang/String;)"),
        ("F","updateRemoteDevicePropertiesCache","(Ljava/lang/String;)"),
    ],
    "Landroid/bluetooth/BluetoothPbap;" : [
        ("F","getClient","()"),
        ("F","getState","()"),
        ("F","isConnected","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;" : [
        ("F","addRfcommServiceRecord","(Ljava/lang/String; Landroid/os/ParcelUuid; I Landroid/os/IBinder;)"),
        ("F","fetchRemoteUuids","(Ljava/lang/String; Landroid/os/ParcelUuid; Landroid/bluetooth/IBluetoothCallback;)"),
        ("F","getAddress","()"),
        ("F","getBluetoothState","()"),
        ("F","getBondState","(Ljava/lang/String;)"),
        ("F","getDiscoverableTimeout","()"),
        ("F","getName","()"),
        ("F","getRemoteClass","(Ljava/lang/String;)"),
        ("F","getRemoteName","(Ljava/lang/String;)"),
        ("F","getRemoteServiceChannel","(Ljava/lang/String; Landroid/os/ParcelUuid;)"),
        ("F","getRemoteUuids","(Ljava/lang/String;)"),
        ("F","getScanMode","()"),
        ("F","getTrustState","(Ljava/lang/String;)"),
        ("F","isDiscovering","()"),
        ("F","isEnabled","()"),
        ("F","listBonds","()"),
        ("F","removeServiceRecord","(I)"),
    ],
    "Landroid/bluetooth/BluetoothAdapter;" : [
        ("C","ACTION_CONNECTION_STATE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_DISCOVERY_FINISHED","Ljava/lang/String;"),
        ("C","ACTION_DISCOVERY_STARTED","Ljava/lang/String;"),
        ("C","ACTION_LOCAL_NAME_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_REQUEST_DISCOVERABLE","Ljava/lang/String;"),
        ("C","ACTION_REQUEST_ENABLE","Ljava/lang/String;"),
        ("C","ACTION_SCAN_MODE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_STATE_CHANGED","Ljava/lang/String;"),
        ("F","cancelDiscovery","()"),
        ("F","disable","()"),
        ("F","enable","()"),
        ("F","getAddress","()"),
        ("F","getBondedDevices","()"),
        ("F","getName","()"),
        ("F","getScanMode","()"),
        ("F","getState","()"),
        ("F","isDiscovering","()"),
        ("F","isEnabled","()"),
        ("F","listenUsingInsecureRfcommWithServiceRecord","(Ljava/lang/String; Ljava/util/UUID;)"),
        ("F","listenUsingRfcommWithServiceRecord","(Ljava/lang/String; Ljava/util/UUID;)"),
        ("F","setName","(Ljava/lang/String;)"),
        ("F","startDiscovery","()"),
        ("F","getAddress","()"),
        ("F","getBondedDevices","()"),
        ("F","getDiscoverableTimeout","()"),
        ("F","getName","()"),
        ("F","getScanMode","()"),
        ("F","getState","()"),
        ("F","isDiscovering","()"),
        ("F","isEnabled","()"),
        ("F","listenUsingRfcommWithServiceRecord","(Ljava/lang/String; Ljava/util/UUID;)"),
    ],
    "Landroid/provider/Settings/Secure;" : [
        ("C","BLUETOOTH_ON","Ljava/lang/String;"),
    ],
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;" : [
        ("F","getBatteryUsageHint","()"),
        ("F","getCurrentHeadset","()"),
        ("F","getPriority","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getState","()"),
        ("F","isConnected","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","startVoiceRecognition","()"),
        ("F","stopVoiceRecognition","()"),
    ],
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;" : [
        ("F","getClient","()"),
        ("F","getState","()"),
        ("F","isConnected","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;" : [
        ("F","getConnectedSinks","()"),
        ("F","getNonDisconnectedSinks","()"),
        ("F","getSinkPriority","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getSinkState","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/provider/Settings/System;" : [
        ("C","AIRPLANE_MODE_RADIOS","Ljava/lang/String;"),
        ("C","BLUETOOTH_DISCOVERABILITY","Ljava/lang/String;"),
        ("C","BLUETOOTH_DISCOVERABILITY_TIMEOUT","Ljava/lang/String;"),
        ("C","BLUETOOTH_ON","Ljava/lang/String;"),
        ("C","RADIO_BLUETOOTH","Ljava/lang/String;"),
        ("C","VOLUME_BLUETOOTH_SCO","Ljava/lang/String;"),
    ],
    "Landroid/bluetooth/BluetoothDevice;" : [
        ("C","ACTION_ACL_CONNECTED","Ljava/lang/String;"),
        ("C","ACTION_ACL_DISCONNECTED","Ljava/lang/String;"),
        ("C","ACTION_ACL_DISCONNECT_REQUESTED","Ljava/lang/String;"),
        ("C","ACTION_BOND_STATE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_CLASS_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_FOUND","Ljava/lang/String;"),
        ("C","ACTION_NAME_CHANGED","Ljava/lang/String;"),
        ("F","createInsecureRfcommSocketToServiceRecord","(Ljava/util/UUID;)"),
        ("F","createRfcommSocketToServiceRecord","(Ljava/util/UUID;)"),
        ("F","getBluetoothClass","()"),
        ("F","getBondState","()"),
        ("F","getName","()"),
        ("F","createRfcommSocketToServiceRecord","(Ljava/util/UUID;)"),
        ("F","fetchUuidsWithSdp","()"),
        ("F","getBondState","()"),
        ("F","getName","()"),
        ("F","getServiceChannel","(Landroid/os/ParcelUuid;)"),
        ("F","getUuids","()"),
    ],
    "Landroid/bluetooth/BluetoothA2dp;" : [
        ("C","ACTION_CONNECTION_STATE_CHANGED","Ljava/lang/String;"),
        ("C","ACTION_PLAYING_STATE_CHANGED","Ljava/lang/String;"),
        ("F","getConnectedDevices","()"),
        ("F","getConnectionState","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getDevicesMatchingConnectionStates","([I)"),
        ("F","isA2dpPlaying","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getConnectedSinks","()"),
        ("F","getNonDisconnectedSinks","()"),
        ("F","getSinkPriority","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getSinkState","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","isSinkConnected","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/bluetooth/BluetoothProfile;" : [
        ("F","getConnectedDevices","()"),
        ("F","getConnectionState","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getDevicesMatchingConnectionStates","([I)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("C","FEATURE_BLUETOOTH","Ljava/lang/String;"),
    ],
    "Landroid/server/BluetoothA2dpService;" : [
        ("F","<init>","(Landroid/content/Context; Landroid/server/BluetoothService;)"),
        ("F","addAudioSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getConnectedSinks","()"),
        ("F","getNonDisconnectedSinks","()"),
        ("F","getSinkPriority","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","getSinkState","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","isSinkDevice","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","lookupSinksMatchingStates","([I)"),
        ("F","onConnectSinkResult","(Ljava/lang/String; B)"),
        ("F","onSinkPropertyChanged","(Ljava/lang/String; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/media/AudioManager;" : [
        ("C","ROUTE_BLUETOOTH","I"),
        ("C","ROUTE_BLUETOOTH_A2DP","I"),
        ("C","ROUTE_BLUETOOTH_SCO","I"),
    ],
},

"android.permission.RESTART_PACKAGES" : {
    "Landroid/app/ActivityManager;" : [
        ("F","killBackgroundProcesses","(Ljava/lang/String;)"),
        ("F","restartPackage","(Ljava/lang/String;)"),
    ],
    "Landroid/app/ActivityManagerNative;" : [
        ("F","killBackgroundProcesses","(Ljava/lang/String;)"),
        ("F","restartPackage","(Ljava/lang/String;)"),
    ],
},

"ASEC_DESTROY" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","destroySecureContainer","(Ljava/lang/String; B)"),
    ],
},

"ASEC_ACCESS" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","getSecureContainerList","()"),
        ("F","getSecureContainerPath","(Ljava/lang/String;)"),
        ("F","isSecureContainerMounted","(Ljava/lang/String;)"),
    ],
},

"com.android.launcher.permission.PRELOAD_WORKSPACE" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher.action.PRELOAD_WORKSPACE","null"),
    ],
},

"android.permission.CHANGE_NETWORK_STATE" : {
    "Landroid/os/INetworkManagementService$Stub$Proxy;" : [
        ("F","attachPppd","(Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","detachPppd","(Ljava/lang/String;)"),
        ("F","disableNat","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","enableNat","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setAccessPoint","(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setInterfaceThrottle","(Ljava/lang/String; I I)"),
        ("F","setIpForwardingEnabled","(B)"),
        ("F","startAccessPoint","(Landroid/net/wifi/WifiConfiguration; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","startUsbRNDIS","()"),
        ("F","stopAccessPoint","()"),
        ("F","stopTethering","()"),
        ("F","stopUsbRNDIS","()"),
        ("F","tetherInterface","(Ljava/lang/String;)"),
        ("F","unregisterObserver","(Landroid/net/INetworkManagementEventObserver;)"),
        ("F","untetherInterface","(Ljava/lang/String;)"),
    ],
    "Landroid/net/ConnectivityManager;" : [
        ("F","requestRouteToHost","(I I)"),
        ("F","setMobileDataEnabled","(B)"),
        ("F","setNetworkPreference","(I)"),
        ("F","setRadio","(I B)"),
        ("F","setRadios","(B)"),
        ("F","startUsingNetworkFeature","(I Ljava/lang/String;)"),
        ("F","stopUsingNetworkFeature","(I Ljava/lang/String;)"),
        ("F","tether","(Ljava/lang/String;)"),
        ("F","untether","(Ljava/lang/String;)"),
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;" : [
        ("F","requestRouteToHost","(I I)"),
        ("F","setMobileDataEnabled","(B)"),
        ("F","setNetworkPreference","(I)"),
        ("F","setRadio","(I B)"),
        ("F","setRadios","(B)"),
        ("F","stopUsingNetworkFeature","(I Ljava/lang/String;)"),
        ("F","tether","(Ljava/lang/String;)"),
        ("F","untether","(Ljava/lang/String;)"),
    ],
},

"android.permission.ACCOUNT_MANAGER" : {
    "Landroid/accounts/AccountManager;" : [
        ("C","KEY_ACCOUNT_MANAGER_RESPONSE","Ljava/lang/String;"),
    ],
    "Landroid/accounts/IAccountAuthenticator$Stub$Proxy;" : [
        ("F","addAccount","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"),
        ("F","confirmCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"),
        ("F","editProperties","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","getAccountRemovalAllowed","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"),
        ("F","getAuthToken","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getAuthTokenLabel","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","hasFeatures","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"),
        ("F","updateCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/AbstractAccountAuthenticator;" : [
        ("F","checkBinderPermission","()"),
        ("F","confirmCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"),
        ("F","editProperties","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","getAccountRemovalAllowed","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"),
        ("F","getAuthToken","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getAuthTokenLabel","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","hasFeatures","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"),
        ("F","updateCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","addAccount","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/AbstractAccountAuthenticator$Transport;" : [
        ("F","addAccount","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle;)"),
        ("F","confirmCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Landroid/os/Bundle;)"),
        ("F","editProperties","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","getAccountRemovalAllowed","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account;)"),
        ("F","getAuthToken","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","getAuthTokenLabel","(Landroid/accounts/IAccountAuthenticatorResponse; Ljava/lang/String;)"),
        ("F","hasFeatures","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"),
        ("F","updateCredentials","(Landroid/accounts/IAccountAuthenticatorResponse; Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
},

"android.permission.DISABLE_KEYGUARD" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","disableKeyguard","(Landroid/os/IBinder; Ljava/lang/String;)"),
        ("F","exitKeyguardSecurely","(Landroid/view/IOnKeyguardExitResult;)"),
        ("F","reenableKeyguard","(Landroid/os/IBinder;)"),
    ],
    "Landroid/app/KeyguardManager;" : [
        ("F","exitKeyguardSecurely","(Landroid/app/KeyguardManager$OnKeyguardExitResult;)"),
    ],
    "Landroid/app/KeyguardManager$KeyguardLock;" : [
        ("F","disableKeyguard","()"),
        ("F","reenableKeyguard","()"),
    ],
},

"android.permission.KILL_BACKGROUND_PROCESSES" : {
    "Landroid/app/ActivityManager;" : [
        ("F","killBackgroundProcesses","(Ljava/lang/String;)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","killBackgroundProcesses","(Ljava/lang/String;)"),
    ],
},

"com.android.launcher.permission.UNINSTALL_SHORTCUT" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher.action.UNINSTALL_SHORTCUT","null"),
    ],
},

"com.android.certinstaller.INSTALL_AS_USER" : {
    "Landroid/content/Intent;" : [
        ("C","android.credentials.INSTALL_AS_USER","null"),
    ],
},

"android.permission.ACCESS_MOCK_LOCATION" : {
    "Landroid/location/LocationManager;" : [
        ("F","addTestProvider","(Ljava/lang/String; B B B B B B B I I)"),
        ("F","clearTestProviderEnabled","(Ljava/lang/String;)"),
        ("F","clearTestProviderLocation","(Ljava/lang/String;)"),
        ("F","clearTestProviderStatus","(Ljava/lang/String;)"),
        ("F","removeTestProvider","(Ljava/lang/String;)"),
        ("F","setTestProviderEnabled","(Ljava/lang/String; B)"),
        ("F","setTestProviderLocation","(Ljava/lang/String; Landroid/location/Location;)"),
        ("F","setTestProviderStatus","(Ljava/lang/String; I Landroid/os/Bundle; J)"),
        ("F","addTestProvider","(Ljava/lang/String; B B B B B B B I I)"),
        ("F","clearTestProviderEnabled","(Ljava/lang/String;)"),
        ("F","clearTestProviderLocation","(Ljava/lang/String;)"),
        ("F","clearTestProviderStatus","(Ljava/lang/String;)"),
        ("F","removeTestProvider","(Ljava/lang/String;)"),
        ("F","setTestProviderEnabled","(Ljava/lang/String; B)"),
        ("F","setTestProviderLocation","(Ljava/lang/String; Landroid/location/Location;)"),
        ("F","setTestProviderStatus","(Ljava/lang/String; I Landroid/os/Bundle; J)"),
    ],
    "Landroid/location/ILocationManager$Stub$Proxy;" : [
        ("F","addTestProvider","(Ljava/lang/String; B B B B B B B I I)"),
        ("F","clearTestProviderEnabled","(Ljava/lang/String;)"),
        ("F","clearTestProviderLocation","(Ljava/lang/String;)"),
        ("F","clearTestProviderStatus","(Ljava/lang/String;)"),
        ("F","removeTestProvider","(Ljava/lang/String;)"),
        ("F","setTestProviderEnabled","(Ljava/lang/String; B)"),
        ("F","setTestProviderLocation","(Ljava/lang/String; Landroid/location/Location;)"),
        ("F","setTestProviderStatus","(Ljava/lang/String; I Landroid/os/Bundle; J)"),
    ],
},

"ASEC_MOUNT_UNMOUNT" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","mountSecureContainer","(Ljava/lang/String; Ljava/lang/String; I)"),
        ("F","unmountSecureContainer","(Ljava/lang/String; B)"),
    ],
},

"android.permission.READ_USER_DICTIONARY" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://user_dictionary"),
        ("F","query","Landroid/provider/UserDictionary$Words;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/userdictionary/UserDictionaryProvider;->CONTENT_URI"),
        ("F","query","Landroid/provider/UserDictionary;->CONTENT_URI"),
    ],
},

"android.permission.SET_PREFERRED_APPLICATIONS" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","addPreferredActivity","(LIntentFilter; I [LComponentName; LComponentName;)"),
        ("F","clearPackagePreferredActivities","(Ljava/lang/String;)"),
        ("F","replacePreferredActivity","(LIntentFilter; I [LComponentName; LComponentName;)"),
        ("F","addPreferredActivity","(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"),
        ("F","clearPackagePreferredActivities","(Ljava/lang/String;)"),
        ("F","replacePreferredActivity","(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","addPreferredActivity","(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"),
        ("F","clearPackagePreferredActivities","(Ljava/lang/String;)"),
        ("F","replacePreferredActivity","(Landroid/content/IntentFilter; I [Landroid/content/ComponentName; Landroid/content/ComponentName;)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","addPreferredActivity","(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)"),
        ("F","clearPackagePreferredActivities","(Ljava/lang/String;)"),
        ("F","replacePreferredActivity","(Landroid/content/IntentFilter; I [L[Landroid/content/ComponentNam; Landroid/content/ComponentName;)"),
    ],
},

"android.permission.ACCESS_ALL_DOWNLOADS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://downloads/all_downloads"),
        ("F","insert","content://downloads/all_downloads"),
        ("F","update","content://downloads/all_downloads"),
        ("F","delete","content://downloads/all_downloads"),
        ("F","query","Landroid/provider/Downloads$Impl;->ALL_DOWNLOADS_CONTENT_URI"),
        ("F","insert","Landroid/provider/Downloads$Impl;->ALL_DOWNLOADS_CONTENT_URI"),
        ("F","update","Landroid/provider/Downloads$Impl;->ALL_DOWNLOADS_CONTENT_URI"),
        ("F","delete","Landroid/provider/Downloads$Impl;->ALL_DOWNLOADS_CONTENT_URI"),
    ],
},

"android.permission.BIND_NFC_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.nfc.cardemulation.action.HOST_APDU_SERVICE","null"),
        ("C","android.nfc.cardemulation.action.OFF_HOST_APDU_SERVICE","null"),
    ],
},

"com.android.voicemail.permission.ADD_VOICEMAIL" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.voicemail"),
        ("F","insert","content://com.android.voicemail"),
        ("F","update","content://com.android.voicemail"),
        ("F","delete","content://com.android.voicemail"),
        ("F","query","Landroid/provider/VoicemailContract$Voicemails;->CONTENT_URI"),
        ("F","insert","Landroid/provider/VoicemailContract$Voicemails;->CONTENT_URI"),
        ("F","update","Landroid/provider/VoicemailContract$Voicemails;->CONTENT_URI"),
        ("F","delete","Landroid/provider/VoicemailContract$Voicemails;->CONTENT_URI"),
        ("F","query","Landroid/provider/VoicemailContract$Status;->CONTENT_URI"),
        ("F","insert","Landroid/provider/VoicemailContract$Status;->CONTENT_URI"),
        ("F","update","Landroid/provider/VoicemailContract$Status;->CONTENT_URI"),
        ("F","delete","Landroid/provider/VoicemailContract$Status;->CONTENT_URI"),
    ],
},

"ASEC_CREATE" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","createSecureContainer","(Ljava/lang/String; I Ljava/lang/String; Ljava/lang/String; I)"),
        ("F","finalizeSecureContainer","(Ljava/lang/String;)"),
    ],
},

"android.permission.WRITE_SYNC_SETTINGS" : {
    "Landroid/app/ContextImpl$ApplicationContentResolver;" : [
        ("F","addPeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"),
        ("F","removePeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","setIsSyncable","(Landroid/accounts/Account; Ljava/lang/String; I)"),
        ("F","setMasterSyncAutomatically","(B)"),
        ("F","setSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String; B)"),
    ],
    "Landroid/content/IContentService$Stub$Proxy;" : [
        ("F","addPeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"),
        ("F","removePeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","setIsSyncable","(Landroid/accounts/Account; Ljava/lang/String; I)"),
        ("F","setMasterSyncAutomatically","(B)"),
        ("F","setSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String; B)"),
    ],
    "Landroid/content/ContentService;" : [
        ("F","addPeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"),
        ("F","removePeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","setIsSyncable","(Landroid/accounts/Account; Ljava/lang/String; I)"),
        ("F","setMasterSyncAutomatically","(B)"),
        ("F","setSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String; B)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","addPeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; J)"),
        ("F","removePeriodicSync","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","setIsSyncable","(Landroid/accounts/Account; Ljava/lang/String; I)"),
        ("F","setMasterSyncAutomatically","(B)"),
        ("F","setSyncAutomatically","(Landroid/accounts/Account; Ljava/lang/String; B)"),
    ],
},

"com.android.email.permission.READ_ATTACHMENT" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.email.attachmentprovider"),
    ],
},

"android.permission.BIND_KEYGUARD_APPWIDGET" : {
    "Landroid/content/Intent;" : [
        ("C","android.appwidget.action.KEYGUARD_APPWIDGET_PICK","null"),
    ],
},

"android.permission.ACCESS_WIFI_STATE" : {
    "Landroid/net/wifi/IWifiManager$Stub$Proxy;" : [
        ("F","getConfiguredNetworks","()"),
        ("F","getConnectionInfo","()"),
        ("F","getDhcpInfo","()"),
        ("F","getNumAllowedChannels","()"),
        ("F","getScanResults","()"),
        ("F","getValidChannelCounts","()"),
        ("F","getWifiApEnabledState","()"),
        ("F","getWifiEnabledState","()"),
        ("F","isMulticastEnabled","()"),
    ],
    "Landroid/net/sip/SipAudioCall;" : [
        ("F","startAudio","()"),
    ],
    "Landroid/net/wifi/WifiManager;" : [
        ("F","getConfiguredNetworks","()"),
        ("F","getConnectionInfo","()"),
        ("F","getDhcpInfo","()"),
        ("F","getNumAllowedChannels","()"),
        ("F","getScanResults","()"),
        ("F","getValidChannelCounts","()"),
        ("F","getWifiApState","()"),
        ("F","getWifiState","()"),
        ("F","isMulticastEnabled","()"),
        ("F","isWifiApEnabled","()"),
        ("F","isWifiEnabled","()"),
    ],
},

"SHUTDOWN" : {
    "Landroid/os/INetworkManagementService$Stub$Proxy;" : [
        ("F","shutdown","()"),
    ],
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","shutdown","(Landroid/os/storage/IMountShutdownObserver;)"),
    ],
    "Landroid/os/IMountService$Stub$Proxy;" : [
        ("F","shutdow","()"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","shutdown","(I)"),
    ],
},

"android.permission.SET_WALLPAPER_HINTS" : {
    "Landroid/app/WallpaperManager;" : [
        ("F","suggestDesiredDimensions","(I I)"),
    ],
    "Landroid/app/IWallpaperManager$Stub$Proxy;" : [
        ("F","setDimensionHints","(I I)"),
    ],
},

"android.permission.BIND_NOTIFICATION_LISTENER_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.service.notification.NotificationListenerService","null"),
    ],
},

"com.android.cts.permissionNormal" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://ctspermissionwithsignaturepathrestricting/foo/bar"),
    ],
},

"android.permission.BIND_CALL_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.services.telephony.common.ICallHandlerService","null"),
    ],
},

"android.permission.BLUETOOTH_ADMIN" : {
    "Landroid/bluetooth/BluetoothPbap;" : [
        ("F","disconnect","()"),
    ],
    "Landroid/content/Intent;" : [
        ("C","android.bluetooth.device.action.CONNECTION_ACCESS_REQUEST android.bluetooth.device.action.CONNECTION_ACCESS_CANCEL","null"),
    ],
    "Landroid/bluetooth/BluetoothHeadset;" : [
        ("F","connectHeadset","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnectHeadset","()"),
        ("F","setPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
    ],
    "Landroid/bluetooth/IBluetoothA2dp$Stub$Proxy;" : [
        ("F","connectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","resumeSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","setSinkPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
        ("F","suspendSink","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/bluetooth/BluetoothAdapter;" : [
        ("F","cancelDiscovery","()"),
        ("F","disable","()"),
        ("F","enable","()"),
        ("F","setName","(Ljava/lang/String;)"),
        ("F","startDiscovery","()"),
        ("F","cancelDiscovery","()"),
        ("F","disable","()"),
        ("F","enable","()"),
        ("F","setDiscoverableTimeout","(I)"),
        ("F","setName","(Ljava/lang/String;)"),
        ("F","startDiscovery","()"),
    ],
    "Landroid/bluetooth/BluetoothA2dp;" : [
        ("F","connectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","resumeSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","setSinkPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
        ("F","suspendSink","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
    "Landroid/server/BluetoothService;" : [
        ("F","cancelBondProcess","(Ljava/lang/String;)"),
        ("F","cancelDiscovery","()"),
        ("F","cancelPairingUserInput","(Ljava/lang/String;)"),
        ("F","createBond","(Ljava/lang/String;)"),
        ("F","disable","()"),
        ("F","disable","(B)"),
        ("F","enable","()"),
        ("F","enable","(B)"),
        ("F","removeBond","(Ljava/lang/String;)"),
        ("F","setDiscoverableTimeout","(I)"),
        ("F","setName","(Ljava/lang/String;)"),
        ("F","setPairingConfirmation","(Ljava/lang/String; B)"),
        ("F","setPasskey","(Ljava/lang/String; I)"),
        ("F","setPin","(Ljava/lang/String; [L;)"),
        ("F","setTrust","(Ljava/lang/String; B)"),
        ("F","startDiscovery","()"),
    ],
    "Landroid/bluetooth/IBluetooth$Stub$Proxy;" : [
        ("F","cancelBondProcess","(Ljava/lang/String;)"),
        ("F","cancelDiscovery","()"),
        ("F","cancelPairingUserInput","(Ljava/lang/String;)"),
        ("F","createBond","(Ljava/lang/String;)"),
        ("F","disable","(B)"),
        ("F","enable","()"),
        ("F","removeBond","(Ljava/lang/String;)"),
        ("F","setDiscoverableTimeout","(I)"),
        ("F","setName","(Ljava/lang/String;)"),
        ("F","setPairingConfirmation","(Ljava/lang/String; B)"),
        ("F","setPasskey","(Ljava/lang/String; I)"),
        ("F","setPin","(Ljava/lang/String; [L;)"),
        ("F","setTrust","(Ljava/lang/String; B)"),
        ("F","startDiscovery","()"),
    ],
    "Landroid/bluetooth/IBluetoothHeadset$Stub$Proxy;" : [
        ("F","connectHeadset","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnectHeadset","()"),
        ("F","setPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
    ],
    "Landroid/bluetooth/IBluetoothPbap$Stub$Proxy;" : [
        ("F","connect","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnect","()"),
    ],
    "Landroid/bluetooth/BluetoothDevice;" : [
        ("F","cancelBondProcess","()"),
        ("F","cancelPairingUserInput","()"),
        ("F","createBond","()"),
        ("F","removeBond","()"),
        ("F","setPairingConfirmation","(B)"),
        ("F","setPasskey","(I)"),
        ("F","setPin","([L;)"),
    ],
    "Landroid/server/BluetoothA2dpService;" : [
        ("F","connectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","disconnectSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","resumeSink","(Landroid/bluetooth/BluetoothDevice;)"),
        ("F","setSinkPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
        ("F","setSinkPriority","(Landroid/bluetooth/BluetoothDevice; I)"),
        ("F","suspendSink","(Landroid/bluetooth/BluetoothDevice;)"),
    ],
},

"PACKAGE_USAGE_STATS" : {
    "Lcom/android/internal/app/IUsageStats$Stub$Proxy;" : [
        ("F","getAllPkgUsageStats","()"),
        ("F","getPkgUsageStats","(LComponentName;)"),
    ],
},

"android.permission.ACCESS_FINE_LOCATION" : {
    "Landroid/webkit/GeolocationPermissions$Callback;" : [
        ("F","invok","()"),
    ],
    "Landroid/location/LocationManager;" : [
        ("C","GPS_PROVIDER","Ljava/lang/String;"),
        ("C","NETWORK_PROVIDER","Ljava/lang/String;"),
        ("C","PASSIVE_PROVIDER","Ljava/lang/String;"),
        ("F","addGpsStatusListener","(Landroid/location/GpsStatus/Listener;)"),
        ("F","addNmeaListener","(Landroid/location/GpsStatus/NmeaListener;)"),
        ("F","_requestLocationUpdates","(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
        ("F","_requestLocationUpdates","(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)"),
        ("F","addGpsStatusListener","(Landroid/location/GpsStatus$Listener;)"),
        ("F","addNmeaListener","(Landroid/location/GpsStatus$NmeaListener;)"),
        ("F","addProximityAlert","(D D F J Landroid/app/PendingIntent;)"),
        ("F","best","(Ljava/util/List;)"),
        ("F","getBestProvider","(Landroid/location/Criteria; B)"),
        ("F","getLastKnownLocation","(Ljava/lang/String;)"),
        ("F","getProvider","(Ljava/lang/String;)"),
        ("F","getProviders","(Landroid/location/Criteria; B)"),
        ("F","getProviders","(B)"),
        ("F","isProviderEnabled","(Ljava/lang/String;)"),
        ("F","requestLocationUpdates","(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
        ("F","requestLocationUpdates","(Ljava/lang/String; J F Landroid/location/LocationListener; Landroid/os/Looper;)"),
        ("F","requestLocationUpdates","(Ljava/lang/String; J F Landroid/location/LocationListener;)"),
        ("F","sendExtraCommand","(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/location/ILocationManager$Stub$Proxy;" : [
        ("F","addGpsStatusListener","(Landroid/location/IGpsStatusListener;)"),
        ("F","addProximityAlert","(D D F J Landroid/app/PendingIntent;)"),
        ("F","getLastKnownLocation","(Ljava/lang/String;)"),
        ("F","getProviderInfo","(Ljava/lang/String;)"),
        ("F","getProviders","(B)"),
        ("F","isProviderEnabled","(Ljava/lang/String;)"),
        ("F","requestLocationUpdates","(Ljava/lang/String; J F Landroid/location/ILocationListener;)"),
        ("F","requestLocationUpdatesPI","(Ljava/lang/String; J F Landroid/app/PendingIntent;)"),
        ("F","sendExtraCommand","(Ljava/lang/String; Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/telephony/TelephonyManager;" : [
        ("F","getCellLocation","()"),
        ("F","getCellLocation","()"),
        ("F","getNeighboringCellInfo","()"),
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
        ("F","getCellLocation","()"),
        ("F","getNeighboringCellInfo","()"),
    ],
    "Landroid/webkit/WebChromeClient;" : [
        ("F","onGeolocationPermissionsShowPrompt","(Ljava/lang/String; Landroid/webkit/GeolocationPermissions/Callback;)"),
    ],
    "Landroid/webkit/GeolocationService;" : [
        ("F","registerForLocationUpdates","()"),
        ("F","setEnableGps","(B)"),
        ("F","start","()"),
    ],
},

"android.permission.REBOOT" : {
    "Landroid/os/IPowerManager$Stub$Proxy;" : [
        ("F","crash","(Ljava/lang/String;)"),
        ("F","reboot","(Ljava/lang/String;)"),
    ],
    "Landroid/os/RecoverySystem;" : [
        ("F","installPackage","(Landroid/content/Context; Ljava/io/File;)"),
        ("F","rebootWipeUserData","(Landroid/content/Context;)"),
        ("F","bootCommand","(Landroid/content/Context; Ljava/lang/String;)"),
        ("F","installPackage","(Landroid/content/Context; Ljava/io/File;)"),
        ("F","rebootWipeUserData","(Landroid/content/Context;)"),
    ],
    "Landroid/content/Intent;" : [
        ("C","IntentResolution","Ljava/lang/String;"),
        ("C","ACTION_REBOOT","Ljava/lang/String;"),
    ],
    "Landroid/os/PowerManager;" : [
        ("F","reboot","(Ljava/lang/String;)"),
        ("F","reboot","(Ljava/lang/String;)"),
    ],
},

"android.permission.PERSISTENT_ACTIVITY" : {
    "Landroid/app/ExpandableListActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/TabActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/Activity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/AliasActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/ListActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","setPersistent","(Landroid/os/IBinder; B)"),
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;" : [
        ("F","setPersistent","(B)"),
    ],
    "Landroid/app/ActivityGroup;" : [
        ("F","setPersistent","(B)"),
    ],
},

"android.permission.USE_CREDENTIALS" : {
    "Landroid/accounts/AccountManager;" : [
        ("F","blockingGetAuthToken","(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ("F","getAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","getAuthToken","(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","invalidateAuthToken","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","blockingGetAuthToken","(Landroid/accounts/Account; Ljava/lang/String; B)"),
        ("F","getAuthToken","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","getAuthToken","(Landroid/accounts/Account; Ljava/lang/String; B Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;" : [
        ("F","getAuthToken","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/AccountManagerService;" : [
        ("F","getAuthToken","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B B Landroid/os/Bundle;)"),
    ],
},

"FORCE_STOP_PACKAGES" : {
    "Landroid/app/ActivityManager;" : [
        ("F","forceStopPackage","(Ljava/lang/String;)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","forceStopPackage","(Ljava/lang/String;)"),
    ],
    "Landroid/app/ActivityManagerNative;" : [
        ("F","forceStopPackage","(Ljava/lang/String;)"),
    ],
},

"android.permission.BROADCAST_WAP_PUSH" : {
    "Landroid/content/Intent;" : [
        ("C","android.provider.Telephony.WAP_PUSH_DELIVER","null"),
    ],
},

"android.permission.MMS_SEND_OUTBOX_MSG" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.MMS_SEND_OUTBOX_MSG","null"),
    ],
},

"android.permission.BIND_TEXT_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.service.textservice.SpellCheckerService","null"),
    ],
},

"com.android.launcher3.permission.READ_SETTINGS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.launcher3.settings"),
    ],
},

"android.permission.DEVICE_POWER" : {
    "Landroid/os/IPowerManager$Stub$Proxy;" : [
        ("F","clearUserActivityTimeout","(J J)"),
        ("F","goToSleep","(J)"),
        ("F","goToSleepWithReason","(J I)"),
        ("F","preventScreenOn","(B)"),
        ("F","setAttentionLight","(B I)"),
        ("F","setBacklightBrightness","(I)"),
        ("F","setPokeLock","(I Landroid/os/IBinder; Ljava/lang/String;)"),
        ("F","userActivityWithForce","(J B B)"),
    ],
    "Landroid/os/PowerManager;" : [
        ("F","goToSleep","(J)"),
        ("F","setBacklightBrightness","(I)"),
    ],
},

"android.permission.ACCESS_BLUETOOTH_SHARE" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.bluetooth.opp/btopp"),
        ("F","insert","content://com.android.bluetooth.opp/btopp"),
        ("F","update","content://com.android.bluetooth.opp/btopp"),
        ("F","delete","content://com.android.bluetooth.opp/btopp"),
        ("F","query","Lcom/android/bluetooth/opp/BluetoothShare;->CONTENT_URI"),
        ("F","insert","Lcom/android/bluetooth/opp/BluetoothShare;->CONTENT_URI"),
        ("F","update","Lcom/android/bluetooth/opp/BluetoothShare;->CONTENT_URI"),
        ("F","delete","Lcom/android/bluetooth/opp/BluetoothShare;->CONTENT_URI"),
    ],
},

"android.permission.EXPAND_STATUS_BAR" : {
    "Landroid/app/IStatusBar$Stub$Proxy;" : [
        ("F","activate","()"),
        ("F","deactivate","()"),
        ("F","toggle","()"),
    ],
    "Landroid/app/StatusBarManager;" : [
        ("F","collapse","()"),
        ("F","expand","()"),
        ("F","toggle","()"),
    ],
},

"android.permission.CONFIRM_FULL_BACKUP" : {
    "Landroid/content/Intent;" : [
        ("C","android.backup.TRANSPORT_HOST","null"),
    ],
},

"android.permission.SET_WALLPAPER" : {
    "Landroid/app/Service;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/view/ContextThemeWrapper;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/content/Context;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/inputmethodservice/AbstractInputMethodService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/ListActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/ExpandableListActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/TabActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/ActivityGroup;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/ContextImpl;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/speech/RecognitionService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/IntentService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/service/urlrenderer/UrlRendererService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/backup/BackupAgent;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/FullBackupAgent;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/backup/BackupAgentHelper;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/content/ContextWrapper;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/accessibilityservice/AccessibilityService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/WallpaperManager;" : [
        ("F","setBitmap","(Landroid/graphics/Bitmap;)"),
        ("F","clear","()"),
        ("F","setBitmap","(Landroid/graphics/Bitmap;)"),
        ("F","setResource","(I)"),
        ("F","setStream","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/AliasActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/service/wallpaper/WallpaperService;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/IWallpaperManager$Stub$Proxy;" : [
        ("F","setWallpaper","(Ljava/lang/String;)"),
    ],
    "Landroid/app/Application;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/app/Activity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/content/MutableContextWrapper;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;" : [
        ("F","clearWallpaper","()"),
        ("F","setWallpaper","(Landroid/graphics/Bitmap;)"),
        ("F","setWallpaper","(Ljava/io/InputStream;)"),
    ],
},

"android.permission.READ_CALL_LOG" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://call_log"),
        ("F","query","Landroid/provider/CallLog$Calls;->CONTENT_FILTER_URI"),
        ("F","query","Landroid/provider/CallLog;->CONTENT_URI"),
        ("F","query","Landroid/provider/CallLog$Calls;->CONTENT_URI"),
        ("F","query","Landroid/provider/CallLog$Calls;->CONTENT_URI_WITH_VOICEMAIL"),
    ],
},

"android.permission.STATUS_BAR" : {
    "Landroid/view/WindowManager/LayoutParams;" : [
        ("C","TYPE_STATUS_BAR","I"),
        ("C","TYPE_STATUS_BAR_PANEL","I"),
        ("C","systemUiVisibility","I"),
        ("C","type","I"),
    ],
    "Landroid/view/View/OnSystemUiVisibilityChangeListener;" : [
        ("F","onSystemUiVisibilityChange","(I)"),
    ],
    "Landroid/app/IStatusBar$Stub$Proxy;" : [
        ("F","addIcon","(Ljava/lang/String; Ljava/lang/String; I I)"),
        ("F","disable","(I Landroid/os/IBinder; Ljava/lang/String;)"),
        ("F","removeIcon","(Landroid/os/IBinder;)"),
        ("F","updateIcon","(Landroid/os/IBinder; Ljava/lang/String; Ljava/lang/String; I I)"),
    ],
    "Landroid/view/View;" : [
        ("C","STATUS_BAR_HIDDEN","I"),
        ("C","STATUS_BAR_VISIBLE","I"),
    ],
    "Landroid/app/StatusBarManager;" : [
        ("F","addIcon","(Ljava/lang/String; I I)"),
        ("F","disable","(I)"),
        ("F","removeIcon","(Landroid/os/IBinder;)"),
        ("F","updateIcon","(Landroid/os/IBinder; Ljava/lang/String; I I)"),
    ],
},

"android.permission.WRITE_USER_DICTIONARY" : {
    "Landroid/provider/UserDictionary$Words;" : [
        ("F","addWord","(Landroid/content/Context; Ljava/lang/String; I I)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://user_dictionary"),
        ("F","update","content://user_dictionary"),
        ("F","delete","content://user_dictionary"),
        ("F","insert","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
        ("F","update","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
        ("F","delete","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
    ],
},

"com.android.browser.permission.READ_HISTORY_BOOKMARKS" : {
    "Landroid/provider/Browser;" : [
        ("C","BOOKMARKS_URI","Landroid/net/Uri;"),
        ("C","SEARCHES_URI","Landroid/net/Uri;"),
        ("F","addSearchUrl","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","canClearHistory","(Landroid/content/ContentResolver;)"),
        ("F","getAllBookmarks","(Landroid/content/ContentResolver;)"),
        ("F","getAllVisitedUrls","(Landroid/content/ContentResolver;)"),
        ("F","requestAllIcons","(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase/IconListener;)"),
        ("F","truncateHistory","(Landroid/content/ContentResolver;)"),
        ("F","updateVisitedHistory","(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
        ("F","addSearchUrl","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","canClearHistory","(Landroid/content/ContentResolver;)"),
        ("F","clearHistory","(Landroid/content/ContentResolver;)"),
        ("F","deleteFromHistory","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","deleteHistoryTimeFrame","(Landroid/content/ContentResolver; J J)"),
        ("F","deleteHistoryWhere","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","getAllBookmarks","(Landroid/content/ContentResolver;)"),
        ("F","getAllVisitedUrls","(Landroid/content/ContentResolver;)"),
        ("F","getVisitedHistory","(Landroid/content/ContentResolver;)"),
        ("F","getVisitedLike","(Landroid/content/ContentResolver; Ljava/lang/String;)"),
        ("F","requestAllIcons","(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)"),
        ("F","truncateHistory","(Landroid/content/ContentResolver;)"),
        ("F","updateVisitedHistory","(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
    ],
    "Landroid/webkit/WebIconDatabase;" : [
        ("F","bulkRequestIconForPageUrl","(Landroid/content/ContentResolver; Ljava/lang/String; Landroid/webkit/WebIconDatabase$IconListener;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://browser"),
        ("F","query","content://com.android.browser.home"),
        ("F","query","content://com.android.browser"),
        ("F","query","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","query","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","query","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","query","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","query","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","query","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","query","Landroid/provider/Browser;->BOOKMARKS_URI"),
    ],
},

"SET_WALLPAPER_COMPONENT" : {
    "Landroid/app/IWallpaperManager$Stub$Proxy;" : [
        ("F","setWallpaperComponent","(Landroid/content/ComponentName;)"),
    ],
},

"android.permission.BIND_PRINT_SPOOLER_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.print.PRINT_DIALOG","null"),
    ],
},

"android.permission.WRITE_EXTERNAL_STORAGE" : {
    "Landroid/os/Build/VERSION_CODES;" : [
        ("C","DONUT","I"),
    ],
    "Landroid/app/DownloadManager/Request;" : [
        ("F","setDestinationUri","(Landroid/net/Uri;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://media/external/"),
        ("F","insert","Lcom/android/music/MusicUtils;->sArtworkUri"),
        ("F","update","Lcom/android/music/MusicUtils;->sArtworkUri"),
        ("F","delete","Lcom/android/music/MusicUtils;->sArtworkUri"),
        ("F","insert","Lcom/android/photos/data/PhotoSetLoader;->GLOBAL_CONTENT_URI"),
        ("F","update","Lcom/android/photos/data/PhotoSetLoader;->GLOBAL_CONTENT_URI"),
        ("F","delete","Lcom/android/photos/data/PhotoSetLoader;->GLOBAL_CONTENT_URI"),
    ],
},

"android.permission.SIGNAL_PERSISTENT_PROCESSES" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","signalPersistentProcesses","(I)"),
    ],
},

"android.permission.GET_PACKAGE_SIZE" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","getPackageSizeInfo","(Ljava/lang/String; LIPackageStatsObserver;)"),
        ("F","getPackageSizeInfo","(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","getPackageSizeInfo","(Ljava/lang/String; Landroid/content/pm/IPackageStatsObserver;)"),
    ],
},

"android.permission.DELETE_CACHE_FILES" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","deleteApplicationCacheFiles","(Ljava/lang/String; LIPackageDataObserver;)"),
        ("F","deleteApplicationCacheFiles","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","deleteApplicationCacheFiles","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","deleteApplicationCacheFiles","(Ljava/lang/String; Landroid/content/pm/IPackageDataObserver;)"),
    ],
},

"android.permission.MANAGE_ACCOUNTS" : {
    "Landroid/accounts/AccountManager;" : [
        ("F","addAccount","(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","clearPassword","(Landroid/accounts/Account;)"),
        ("F","confirmCredentials","(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","editProperties","(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","getAuthTokenByFeatures","(Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","invalidateAuthToken","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","removeAccount","(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)"),
        ("F","updateCredentials","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback<android/os/Bundle>; Landroid/os/Handler;)"),
        ("F","addAccount","(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","clearPassword","(Landroid/accounts/Account;)"),
        ("F","confirmCredentials","(Landroid/accounts/Account; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","editProperties","(Ljava/lang/String; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","invalidateAuthToken","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","removeAccount","(Landroid/accounts/Account; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","updateCredentials","(Landroid/accounts/Account; Ljava/lang/String; Landroid/os/Bundle; Landroid/app/Activity; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;" : [
        ("F","addAcount","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)"),
        ("F","clearPassword","(Landroid/accounts/Account;)"),
        ("F","confirmCredentials","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)"),
        ("F","editProperties","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)"),
        ("F","invalidateAuthToken","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","removeAccount","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)"),
        ("F","updateCredentials","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/AccountManagerService;" : [
        ("F","addAcount","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; B Landroid/os/Bundle;)"),
        ("F","checkManageAccountsOrUseCredentialsPermissions","()"),
        ("F","checkManageAccountsPermission","()"),
        ("F","clearPassword","(Landroid/accounts/Account;)"),
        ("F","confirmCredentials","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Landroid/os/Bundle; B)"),
        ("F","editProperties","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; B)"),
        ("F","invalidateAuthToken","(Ljava/lang/String; Ljava/lang/String;)"),
        ("F","removeAccount","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account;)"),
        ("F","updateCredentials","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; Ljava/lang/String; B Landroid/os/Bundle;)"),
    ],
},

"android.permission.READ_EXTERNAL_STORAGE" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://media/external/"),
        ("F","query","Lcom/android/music/MusicUtils;->sArtworkUri"),
        ("F","query","Lcom/android/photos/data/PhotoSetLoader;->GLOBAL_CONTENT_URI"),
    ],
},

"android.permission.SET_PROCESS_LIMIT" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","setProcessForeground","(Landroid/os/IBinder; I B)"),
        ("F","setProcessLimit","(I)"),
    ],
},

"android.permission.MODIFY_PHONE_STATE" : {
    "Lcom/android/internal/telephony/ITelephonyRegistry$Stub$Proxy;" : [
        ("F","notifyCallForwardingChanged","(B)"),
        ("F","notifyCallState","(I Ljava/lang/String;)"),
        ("F","notifyCellLocation","(Landroid/os/Bundle;)"),
        ("F","notifyDataActivity","(I)"),
        ("F","notifyDataConnection","(I B Ljava/lang/String; Ljava/lang/String; [Ljava/lang/String; Ljava/lang/String; I)"),
        ("F","notifyDataConnectionFailed","(Ljava/lang/String;)"),
        ("F","notifyMessageWaitingChanged","(B)"),
        ("F","notifyServiceState","(Landroid/telephony/ServiceState;)"),
        ("F","notifySignalStrength","(Landroid/telephony/SignalStrength;)"),
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
        ("F","answerRingingCall","()"),
        ("F","cancelMissedCallsNotification","()"),
        ("F","disableApnType","(Ljava/lang/String;)"),
        ("F","disableDataConnectivity","()"),
        ("F","enableApnType","(Ljava/lang/String;)"),
        ("F","enableDataConnectivity","()"),
        ("F","handlePinMmi","(Ljava/lang/String;)"),
        ("F","setRadio","(B)"),
        ("F","silenceRinger","()"),
        ("F","supplyPin","(Ljava/lang/String;)"),
        ("F","toggleRadioOnOff","()"),
    ],
    "Landroid/net/MobileDataStateTracker;" : [
        ("F","reconnect","()"),
        ("F","setRadio","(B)"),
        ("F","teardown","()"),
    ],
},

"android.permission.BIND_APPWIDGET" : {
    "Landroid/appwidget/AppWidgetManager;" : [
        ("F","bindAppWidgetId","(I Landroid/content/ComponentName;)"),
    ],
    "Lcom/android/internal/appwidget/IAppWidgetService$Stub$Proxy;" : [
        ("F","bindAppWidgetId","(I LComponentName;)"),
    ],
},

"com.android.frameworks.coretests.permission.TEST_GRANTED" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.frameworks.coretests.activity.BROADCAST_LOCAL_GRANTED","null"),
        ("C","com.android.frameworks.coretests.activity.BROADCAST_REMOTE_GRANTED","null"),
        ("C","com.android.frameworks.coretests.activity.SERVICE_LOCAL_GRANTED","null"),
    ],
},

"android.app.cts.permission.TEST_DENIED" : {
    "Landroid/content/Intent;" : [
        ("C","android.app.cts.activity.SERVICE_LOCAL_DENIED","null"),
    ],
},

"com.android.launcher.permission.READ_SETTINGS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.launcher2.settings"),
    ],
},

"android.permission.INSTALL_LOCATION_PROVIDER" : {
    "Landroid/location/ILocationManager$Stub$Proxy;" : [
        ("F","reportLocation","(Landroid/location/Location; B)"),
    ],
},

"com.android.alarm.permission.SET_ALARM" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.SET_ALARM","null"),
        ("C","android.intent.action.SET_TIMER","null"),
        ("C","android.intent.action.SHOW_ALARMS","null"),
    ],
    "Landroid/provider/AlarmClock;" : [
        ("C","ACTION_SET_ALARM","Ljava/lang/String;"),
        ("C","EXTRA_HOUR","Ljava/lang/String;"),
        ("C","EXTRA_MESSAGE","Ljava/lang/String;"),
        ("C","EXTRA_MINUTES","Ljava/lang/String;"),
        ("C","EXTRA_SKIP_UI","Ljava/lang/String;"),
    ],
},

"android.permission.ACCESS_NETWORK_STATE" : {
    "Landroid/net/ConnectivityManager;" : [
        ("F","getActiveNetworkInfo","()"),
        ("F","getAllNetworkInfo","()"),
        ("F","getLastTetherError","(Ljava/lang/String;)"),
        ("F","getMobileDataEnabled","()"),
        ("F","getNetworkInfo","(I)"),
        ("F","getNetworkPreference","()"),
        ("F","getTetherableIfaces","()"),
        ("F","getTetherableUsbRegexs","()"),
        ("F","getTetherableWifiRegexs","()"),
        ("F","getTetheredIfaces","()"),
        ("F","getTetheringErroredIfaces","()"),
        ("F","isTetheringSupported","()"),
    ],
    "Landroid/net/IConnectivityManager$Stub$Proxy;" : [
        ("F","getActiveNetworkInfo","()"),
        ("F","getAllNetworkInfo","()"),
        ("F","getLastTetherError","(Ljava/lang/String;)"),
        ("F","getMobileDataEnabled","()"),
        ("F","getNetworkInfo","(I)"),
        ("F","getNetworkPreference","()"),
        ("F","getTetherableIfaces","()"),
        ("F","getTetherableUsbRegexs","()"),
        ("F","getTetherableWifiRegexs","()"),
        ("F","getTetheredIfaces","()"),
        ("F","getTetheringErroredIfaces","()"),
        ("F","isTetheringSupported","()"),
        ("F","startUsingNetworkFeature","(I Ljava/lang/String; Landroid/os/IBinder;)"),
    ],
    "Landroid/net/http/RequestQueue;" : [
        ("F","enablePlatformNotifications","()"),
        ("F","setProxyConfig","()"),
    ],
    "Landroid/net/ThrottleManager;" : [
        ("F","getByteCount","(Ljava/lang/String; I I I)"),
        ("F","getCliffLevel","(Ljava/lang/String; I)"),
        ("F","getCliffThreshold","(Ljava/lang/String; I)"),
        ("F","getHelpUri","()"),
        ("F","getPeriodStartTime","(Ljava/lang/String;)"),
        ("F","getResetTime","(Ljava/lang/String;)"),
    ],
    "Landroid/net/IThrottleManager$Stub$Proxy;" : [
        ("F","getByteCount","(Ljava/lang/String; I I I)"),
        ("F","getCliffLevel","(Ljava/lang/String; I)"),
        ("F","getCliffThreshold","(Ljava/lang/String; I)"),
        ("F","getHelpUri","()"),
        ("F","getPeriodStartTime","(Ljava/lang/String;)"),
        ("F","getResetTime","(Ljava/lang/String;)"),
        ("F","getThrottle","(Ljava/lang/String;)"),
    ],
    "Landroid/net/NetworkInfo;" : [
        ("F","isConnectedOrConnecting","()"),
    ],
    "Landroid/os/INetworkManagementService$Stub$Proxy;" : [
        ("F","getDnsForwarders","()"),
        ("F","getInterfaceRxCounter","(Ljava/lang/String;)"),
        ("F","getInterfaceRxThrottle","(Ljava/lang/String;)"),
        ("F","getInterfaceTxCounter","(Ljava/lang/String;)"),
        ("F","getInterfaceTxThrottle","(Ljava/lang/String;)"),
        ("F","getIpForwardingEnabled","()"),
        ("F","isTetheringStarted","()"),
        ("F","isUsbRNDISStarted","()"),
        ("F","listInterfaces","()"),
        ("F","listTetheredInterfaces","()"),
        ("F","listTtys","()"),
    ],
},

"android.permission.WRITE_SETTINGS" : {
    "Landroid/os/IPowerManager$Stub$Proxy;" : [
        ("F","setStayOnSetting","(I)"),
    ],
    "Landroid/provider/Settings$Bookmarks;" : [
        ("F","add","(Landroid/content/ContentResolver; Landroid/content/Intent; Ljava/lang/String; Ljava/lang/String; C I)"),
        ("F","getIntentForShortcut","(Landroid/content/ContentResolver; C)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://settings"),
        ("F","update","content://settings"),
        ("F","delete","content://settings"),
        ("F","insert","Landroid/provider/Settings$System;->CONTENT_URI"),
        ("F","update","Landroid/provider/Settings$System;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Settings$System;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Settings$Secure;->CONTENT_URI"),
        ("F","update","Landroid/provider/Settings$Secure;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Settings$Secure;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Settings$Bookmarks;->CONTENT_URI"),
        ("F","update","Landroid/provider/Settings$Bookmarks;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Settings$Bookmarks;->CONTENT_URI"),
        ("F","insert","Landroid/provider/Settings$Global;->CONTENT_URI"),
        ("F","update","Landroid/provider/Settings$Global;->CONTENT_URI"),
        ("F","delete","Landroid/provider/Settings$Global;->CONTENT_URI"),
    ],
    "Landroid/provider/Settings$System;" : [
        ("F","putConfiguration","(Landroid/content/ContentResolver; Landroid/content/res/Configuration;)"),
        ("F","putFloat","(Landroid/content/ContentResolver; Ljava/lang/String; F)"),
        ("F","putInt","(Landroid/content/ContentResolver; Ljava/lang/String; I)"),
        ("F","putLong","(Landroid/content/ContentResolver; Ljava/lang/String; J)"),
        ("F","putString","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setShowGTalkServiceStatus","(Landroid/content/ContentResolver; B)"),
    ],
    "Landroid/os/IMountService$Stub$Proxy;" : [
        ("F","setAutoStartUm","()"),
        ("F","setPlayNotificationSound","()"),
    ],
    "Landroid/media/RingtoneManager;" : [
        ("F","setActualDefaultRingtoneUri","(Landroid/content/Context; I Landroid/net/Uri;)"),
    ],
    "Landroid/server/BluetoothService;" : [
        ("F","persistBluetoothOnSetting","(B)"),
    ],
    "Landroid/provider/Settings$Secure;" : [
        ("F","putFloat","(Landroid/content/ContentResolver; Ljava/lang/String; F)"),
        ("F","putInt","(Landroid/content/ContentResolver; Ljava/lang/String; I)"),
        ("F","putLong","(Landroid/content/ContentResolver; Ljava/lang/String; J)"),
        ("F","putString","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","setLocationProviderEnabled","(Landroid/content/ContentResolver; Ljava/lang/String; B)"),
    ],
},

"android.permission.PERFORM_CDMA_PROVISIONING" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.phone.PERFORM_CDMA_PROVISIONING","null"),
    ],
},

"com.android.browser.permission.PRELOAD" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.PRELOAD","null"),
    ],
},

"com.android.launcher3.permission.INSTALL_SHORTCUT" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher3.action.INSTALL_SHORTCUT","null"),
    ],
},

"android.permission.INSTALL_PACKAGES" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","installPackage","(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"),
        ("F","installPackage","(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","installPackage","(Landroid/net/Uri; LIPackageInstallObserver; I Ljava/lang/String;)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","installPackage","(Landroid/net/Uri; Landroid/content/pm/IPackageInstallObserver; I Ljava/lang/String;)"),
    ],
},

"android.permission.INJECT_EVENTS" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","injectKeyEvent","(Landroid/view/KeyEvent; B)"),
        ("F","injectPointerEvent","(Landroid/view/MotionEvent; B)"),
        ("F","injectTrackballEvent","(Landroid/view/MotionEvent; B)"),
    ],
    "Landroid/app/Instrumentation;" : [
        ("F","invokeContextMenuAction","(Landroid/app/Activity; I I)"),
        ("F","sendCharacterSync","(I)"),
        ("F","sendKeyDownUpSync","(I)"),
        ("F","sendKeySync","(Landroid/view/KeyEvent;)"),
        ("F","sendPointerSync","(Landroid/view/MotionEvent;)"),
        ("F","sendStringSync","(Ljava/lang/String;)"),
        ("F","sendTrackballEventSync","(Landroid/view/MotionEvent;)"),
    ],
},

"android.permission.SET_ORIENTATION" : {
    "Landroid/view/IWindowManager$Stub$Proxy;" : [
        ("F","setRotation","(I B I)"),
    ],
},

"android.permission.SET_ACTIVITY_WATCHER" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","profileControl","(Ljava/lang/String; B Ljava/lang/String; Landroid/os/ParcelFileDescriptor;)"),
        ("F","setActivityController","(Landroid/app/IActivityController;)"),
    ],
},

"android.permission.BROADCAST_STICKY" : {
    "Landroid/app/Service;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/view/ContextThemeWrapper;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/content/Context;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/inputmethodservice/AbstractInputMethodService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/ListActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/ExpandableListActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/TabActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/ActivityGroup;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","unbroadcastIntent","(Landroid/app/IApplicationThread; Landroid/content/Intent;)"),
    ],
    "Landroid/app/ContextImpl;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/speech/RecognitionService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/IntentService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/service/urlrenderer/UrlRendererService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/backup/BackupAgent;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/FullBackupAgent;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/backup/BackupAgentHelper;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/content/ContextWrapper;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/accessibilityservice/AccessibilityService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/AliasActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/service/wallpaper/WallpaperService;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/Application;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/app/Activity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/content/MutableContextWrapper;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/GrantCredentialsPermissionActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
    "Landroid/accounts/AccountAuthenticatorActivity;" : [
        ("F","removeStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyBroadcast","(Landroid/content/Intent;)"),
        ("F","sendStickyOrderedBroadcast","(Landroid/content/Intent; Landroid/content/BroadcastReceiver; Landroid/os/Handler; I Ljava/lang/String; Landroid/os/Bundle;)"),
    ],
},

"android.permission.SET_DEBUG_APP" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","setDebugApp","(Ljava/lang/String; B B)"),
    ],
},

"android.permission.READ_SMS" : {
    "Landroid/provider/Telephony$Sms$Sent;" : [
        ("F","addMessage","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)"),
    ],
    "Landroid/provider/Telephony$Mms;" : [
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/provider/Telephony$Sms;" : [
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin; Ljava/lang/String; Ljava/lang/String;)"),
        ("F","query","(Landroid/content/ContentResolver; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/provider/Telephony$Sms$Draft;" : [
        ("F","addMessage","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long;)"),
    ],
    "Landroid/provider/Telephony$Threads;" : [
        ("F","getOrCreateThreadId","(Landroid/content/Context; Ljava/lang/String;)"),
        ("F","getOrCreateThreadId","(Landroid/content/Context; Ljava/util/Set;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.mms.SuggestionsProvider"),
        ("F","query","content://mms"),
        ("F","query","content://mms-sms"),
        ("F","query","content://sms"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_LOCKED_URI"),
        ("F","query","Landroid/provider/Telephony$Mms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Threads;->OBSOLETE_THREADS_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Draft;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->SEARCH_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Threads;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Threads;->THREAD_ID_CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Mms$Rate;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Mms;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_CONVERSATIONS_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->ICC_URI"),
        ("F","query","Landroid/provider/Telephony$Sms;->CONTENT_URI"),
        ("F","query","Lcom/android/providers/telephony/SmsProvider;->NOTIFICATION_URI"),
        ("F","query","Landroid/provider/Telephony$Mms;->REPORT_STATUS_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_UNDELIVERED_URI"),
        ("F","query","Landroid/provider/Telephony$Mms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/internal/telephony/SmsBroadcastUndelivered;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Mms;->REPORT_REQUEST_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_DRAFT_URI"),
        ("F","query","Landroid/provider/Telephony$Mms$Outbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Sent;->CONTENT_URI"),
        ("F","query","Lcom/android/internal/telephony/InboundSmsHandler;->sRawUri"),
        ("F","query","Landroid/provider/Telephony$Mms$Inbox;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms$PendingMessages;->CONTENT_URI"),
        ("F","query","Landroid/provider/Telephony$MmsSms;->CONTENT_FILTER_BYPHONE_URI"),
        ("F","query","Landroid/provider/Telephony$Sms$Conversations;->CONTENT_URI"),
    ],
    "Landroid/provider/Telephony$Sms$Inbox;" : [
        ("F","addMessage","(Landroid/content/ContentResolver; Ljava/lang/String; Ljava/lang/String; Ljava/lang/String; Ljava/lang/Long; B)"),
    ],
},

"android.permission.VIBRATE" : {
    "Landroid/os/Vibrator;" : [
        ("F","cancel","()"),
        ("F","vibrate","([L; I)"),
        ("F","vibrate","(J)"),
    ],
    "Landroid/os/IVibratorService$Stub$Proxy;" : [
        ("F","cancelVibrate","(Landroid/os/IBinder;)"),
        ("F","vibrate","(J Landroid/os/IBinder;)"),
        ("F","vibratePattern","([L; I Landroid/os/IBinder;)"),
    ],
    "Landroid/app/Notification;" : [
        ("C","DEFAULT_VIBRATE","I"),
        ("C","defaults","I"),
    ],
    "Landroid/app/Notification/Builder;" : [
        ("F","setDefaults","(I)"),
    ],
    "Landroid/provider/Settings/System;" : [
        ("C","VIBRATE_ON","Ljava/lang/String;"),
    ],
    "Landroid/app/NotificationManager;" : [
        ("F","notify","(I Landroid/app/Notification;)"),
        ("F","notify","(Ljava/lang/String; I Landroid/app/Notification;)"),
    ],
    "Landroid/media/AudioManager;" : [
        ("C","EXTRA_RINGER_MODE","Ljava/lang/String;"),
        ("C","EXTRA_VIBRATE_SETTING","Ljava/lang/String;"),
        ("C","EXTRA_VIBRATE_TYPE","Ljava/lang/String;"),
        ("C","FLAG_REMOVE_SOUND_AND_VIBRATE","I"),
        ("C","FLAG_VIBRATE","I"),
        ("C","RINGER_MODE_VIBRATE","I"),
        ("C","VIBRATE_SETTING_CHANGED_ACTION","Ljava/lang/String;"),
        ("C","VIBRATE_SETTING_OFF","I"),
        ("C","VIBRATE_SETTING_ON","I"),
        ("C","VIBRATE_SETTING_ONLY_SILENT","I"),
        ("C","VIBRATE_TYPE_NOTIFICATION","I"),
        ("C","VIBRATE_TYPE_RINGER","I"),
        ("F","getRingerMode","()"),
        ("F","getVibrateSetting","(I)"),
        ("F","setRingerMode","(I)"),
        ("F","setVibrateSetting","(I I)"),
        ("F","shouldVibrate","(I)"),
    ],
},

"STOP_APP_SWITCHES" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","resumeAppSwitches","()"),
        ("F","stopAppSwitches","()"),
    ],
},

"android.permission.BATTERY_STATS" : {
    "Lcom/android/internal/app/IBatteryStats$Stub$Proxy;" : [
        ("F","getAwakeTimeBattery","()"),
        ("F","getAwakeTimePlugged","()"),
        ("F","getStatistics","()"),
    ],
},

"android.permission.CHANGE_COMPONENT_ENABLED_STATE" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","setApplicationEnabledSetting","(Ljava/lang/String; I I)"),
        ("F","setComponentEnabledSetting","(LComponentName; I I)"),
        ("F","setApplicationEnabledSetting","(Ljava/lang/String; I I)"),
        ("F","setComponentEnabledSetting","(Landroid/content/ComponentName; I I)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","setApplicationEnabledSetting","(Ljava/lang/String; I I)"),
        ("F","setComponentEnabledSetting","(Landroid/content/ComponentName; I I)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","setApplicationEnabledSetting","(Ljava/lang/String; I I)"),
        ("F","setComponentEnabledSetting","(Landroid/content/ComponentName; I I)"),
    ],
},

"android.permission.CAMERA" : {
    "Landroid/content/Intent;" : [
        ("C","IntentResolution","Ljava/lang/String;"),
        ("C","ACTION_CAMERA_BUTTON","Ljava/lang/String;"),
    ],
    "Landroid/provider/ContactsContract/StatusColumns;" : [
        ("C","CAPABILITY_HAS_CAMERA","I"),
    ],
    "Landroid/hardware/Camera/Parameters;" : [
        ("F","setRotation","(I)"),
    ],
    "Landroid/media/MediaRecorder;" : [
        ("F","setVideoSource","(I)"),
    ],
    "Landroid/hardware/Camera/ErrorCallback;" : [
        ("F","onError","(I Landroid/hardware/Camera;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("C","FEATURE_CAMERA","Ljava/lang/String;"),
        ("C","FEATURE_CAMERA_AUTOFOCUS","Ljava/lang/String;"),
        ("C","FEATURE_CAMERA_FLASH","Ljava/lang/String;"),
        ("C","FEATURE_CAMERA_FRONT","Ljava/lang/String;"),
    ],
    "Landroid/bluetooth/BluetoothClass/Device;" : [
        ("C","AUDIO_VIDEO_VIDEO_CAMERA","I"),
    ],
    "Landroid/view/KeyEvent;" : [
        ("C","KEYCODE_CAMERA","I"),
    ],
    "Landroid/provider/MediaStore;" : [
        ("C","INTENT_ACTION_STILL_IMAGE_CAMERA","Ljava/lang/String;"),
        ("C","INTENT_ACTION_VIDEO_CAMERA","Ljava/lang/String;"),
    ],
    "Landroid/media/MediaRecorder/VideoSource;" : [
        ("C","CAMERA","I"),
    ],
    "Landroid/hardware/Camera/CameraInfo;" : [
        ("C","CAMERA_FACING_BACK","I"),
        ("C","CAMERA_FACING_FRONT","I"),
        ("C","facing","I"),
    ],
    "Landroid/hardware/Camera;" : [
        ("C","CAMERA_ERROR_SERVER_DIED","I"),
        ("C","CAMERA_ERROR_UNKNOWN","I"),
        ("F","setDisplayOrientation","(I)"),
        ("F","native_setup","(Ljava/lang/Object;)"),
        ("F","open","()"),
    ],
},

"android.permission.GLOBAL_SEARCH" : {
    "Landroid/server/search/Searchables;" : [
        ("F","buildSearchableList","()"),
        ("F","findGlobalSearchActivity","()"),
    ],
    "Landroid/app/SearchManager;" : [
        ("C","EXTRA_SELECT_QUERY","Ljava/lang/String;"),
        ("C","INTENT_ACTION_GLOBAL_SEARCH","Ljava/lang/String;"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://browser/bookmarks/search_suggest_query"),
        ("F","query","content://com.android.browser/bookmarks/search_suggest_query"),
        ("F","query","content://com.android.contacts/contacts/.*/photo"),
        ("F","query","content://com.android.contacts/search_suggest_query"),
        ("F","query","content://com.android.contacts/search_suggest_shortcut"),
        ("F","query","content://com.android.mms.SuggestionsProvider/search_suggest_query"),
        ("F","query","content://com.android.mms.SuggestionsProvider/search_suggest_shortcut"),
        ("F","query","content://contacts/contacts/.*/photo"),
        ("F","query","content://contacts/search_suggest_query"),
        ("F","query","content://contacts/search_suggest_shortcut"),
    ],
},

"com.android.smspush.WAPPUSH_MANAGER_BIND" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.internal.telephony.IWapPushManager","null"),
    ],
},

"com.android.cts.permissionWithSignature" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://ctspermissionwithsignaturegranting"),
        ("F","insert","content://ctspermissionwithsignaturegranting"),
        ("F","update","content://ctspermissionwithsignaturegranting"),
        ("F","delete","content://ctspermissionwithsignaturegranting"),
        ("F","query","content://ctspermissionwithsignaturepath/foo"),
        ("F","query","content://ctspermissionwithsignaturepathrestricting/foo"),
        ("F","query","content://ctspermissionwithsignaturepath/yes"),
        ("F","query","content://ctspermissionwithsignature"),
        ("F","insert","content://ctspermissionwithsignature"),
        ("F","update","content://ctspermissionwithsignature"),
        ("F","delete","content://ctspermissionwithsignature"),
    ],
},

"android.permission.BIND_ACCESSIBILITY_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.accessibilityservice.AccessibilityService","null"),
    ],
},

"com.android.launcher.permission.WRITE_SETTINGS" : {
    "Landroid/content/ContentResolver;" : [
        ("F","insert","content://com.android.launcher2.settings"),
        ("F","update","content://com.android.launcher2.settings"),
        ("F","delete","content://com.android.launcher2.settings"),
    ],
},

"android.permission.MOUNT_FORMAT_FILESYSTEMS" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","formatVolume","(Ljava/lang/String;)"),
    ],
    "Landroid/os/IMountService$Stub$Proxy;" : [
        ("F","formatMedi","()"),
    ],
},

"android.permission.REORDER_TASKS" : {
    "Landroid/app/ActivityManager;" : [
        ("F","moveTaskToFront","(I I)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","moveTaskBackwards","(I)"),
        ("F","moveTaskToBack","(I)"),
        ("F","moveTaskToFront","(I)"),
    ],
},

"android.permission.CONTROL_LOCATION_UPDATES" : {
    "Landroid/telephony/TelephonyManager;" : [
        ("F","disableLocationUpdates","()"),
        ("F","enableLocationUpdates","()"),
    ],
    "Lcom/android/internal/telephony/ITelephony$Stub$Proxy;" : [
        ("F","disableLocationUpdates","()"),
        ("F","enableLocationUpdates","()"),
    ],
},

"com.android.gallery3d.filtershow.permission.READ" : {
    "Landroid/content/ContentResolver;" : [
        ("F","query","content://com.android.gallery3d.filtershow.provider.SharedImageProvider"),
        ("F","query","Lcom/android/gallery3d/filtershow/provider/SharedImageProvider;->CONTENT_URI"),
    ],
},

"android.permission.SET_ALWAYS_FINISH" : {
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","setAlwaysFinish","(B)"),
    ],
},

"android.permission.GET_ACCOUNTS" : {
    "Landroid/accounts/AccountManagerService;" : [
        ("F","checkReadAccountsPermission","()"),
        ("F","getAccounts","(Ljava/lang/String;)"),
        ("F","getAccountsByFeatures","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ("F","hasFeatures","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/accounts/AccountManager$GetAuthTokenByTypeAndFeaturesTask;" : [
        ("F","doWork","()"),
        ("F","start","()"),
    ],
    "Landroid/accounts/AccountManager;" : [
        ("F","getAccounts","()"),
        ("F","getAccountsByType","(Ljava/lang/String;)"),
        ("F","getAccountsByTypeAndFeatures","(Ljava/lang/String; [Ljava/lang/String; [Landroid/accounts/AccountManagerCallback<android/accounts/Account[; Landroid/os/Handler;)"),
        ("F","hasFeatures","(Landroid/accounts/Account; [Ljava/lang/String; Landroid/accounts/AccountManagerCallback<java/lang/Boolean>; Landroid/os/Handler;)"),
        ("F","addOnAccountsUpdatedListener","(Landroid/accounts/OnAccountsUpdateListener; Landroid/os/Handler; B)"),
        ("F","getAccounts","()"),
        ("F","getAccountsByType","(Ljava/lang/String;)"),
        ("F","getAccountsByTypeAndFeatures","(Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","getAuthTokenByFeatures","(Ljava/lang/String; Ljava/lang/String; [L[Ljava/lang/Strin; Landroid/app/Activity; Landroid/os/Bundle; Landroid/os/Bundle; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
        ("F","hasFeatures","(Landroid/accounts/Account; [L[Ljava/lang/Strin; Landroid/accounts/AccountManagerCallback; Landroid/os/Handler;)"),
    ],
    "Landroid/content/ContentResolver;" : [
        ("F","query","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","insert","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","update","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","delete","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI_DEFAULT_FOLDER"),
        ("F","query","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Settings;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/BrowserProvider2$Thumbnails;->CONTENT_URI"),
        ("F","query","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","insert","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","update","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","delete","Landroid/provider/Browser;->SEARCHES_URI"),
        ("F","query","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Accounts;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$ImageMappings;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Searches;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","insert","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","update","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","delete","Landroid/provider/BrowserContract;->AUTHORITY_URI"),
        ("F","query","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Bookmarks;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/SnapshotProvider$Snapshots;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","insert","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","update","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","delete","Lcom/android/browser/provider/BrowserProvider2$OmniboxSuggestions;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Images;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$Combined;->CONTENT_URI"),
        ("F","query","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","insert","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","update","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","delete","Lcom/android/browser/provider/SnapshotProvider;->AUTHORITY_URI"),
        ("F","query","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$History;->CONTENT_URI"),
        ("F","query","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","insert","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","update","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","delete","Landroid/provider/BrowserContract$SyncState;->CONTENT_URI"),
        ("F","query","Landroid/provider/Browser;->BOOKMARKS_URI"),
        ("F","insert","Landroid/provider/Browser;->BOOKMARKS_URI"),
        ("F","update","Landroid/provider/Browser;->BOOKMARKS_URI"),
        ("F","delete","Landroid/provider/Browser;->BOOKMARKS_URI"),
    ],
    "Landroid/accounts/AccountManager$AmsTask;" : [
        ("F","doWork","()"),
        ("F","start","()"),
    ],
    "Landroid/accounts/IAccountManager$Stub$Proxy;" : [
        ("F","getAccounts","(Ljava/lang/String;)"),
        ("F","getAccountsByFeatures","(Landroid/accounts/IAccountManagerResponse; Ljava/lang/String; [L[Ljava/lang/Strin;)"),
        ("F","hasFeatures","(Landroid/accounts/IAccountManagerResponse; Landroid/accounts/Account; [L[Ljava/lang/Strin;)"),
    ],
    "Landroid/content/ContentService;" : [
        ("F","<init>","(Landroid/content/Context; B)"),
        ("F","main","(Landroid/content/Context; B)"),
    ],
},

"android.permission.BIND_PRINT_SERVICE" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.MAIN","null"),
        ("C","android.printservice.PrintService","null"),
    ],
},

"android.permission.CLEAR_APP_CACHE" : {
    "Landroid/app/ContextImpl$ApplicationPackageManager;" : [
        ("F","freeStorage","(J LIntentSender;)"),
        ("F","freeStorageAndNotify","(J LIPackageDataObserver;)"),
        ("F","freeStorage","(J Landroid/content/IntentSender;)"),
        ("F","freeStorageAndNotify","(J Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/content/pm/PackageManager;" : [
        ("F","freeStorage","(J Landroid/content/IntentSender;)"),
        ("F","freeStorageAndNotify","(J Landroid/content/pm/IPackageDataObserver;)"),
    ],
    "Landroid/content/pm/IPackageManager$Stub$Proxy;" : [
        ("F","freeStorage","(J Landroid/content/IntentSender;)"),
        ("F","freeStorageAndNotify","(J Landroid/content/pm/IPackageDataObserver;)"),
    ],
},

"android.permission.MOUNT_UNMOUNT_FILESYSTEMS" : {
    "Landroid/os/storage/IMountService$Stub$Proxy;" : [
        ("F","getStorageUsers","(Ljava/lang/String;)"),
        ("F","mountVolume","(Ljava/lang/String;)"),
        ("F","setUsbMassStorageEnabled","(B)"),
        ("F","unmountVolume","(Ljava/lang/String; B)"),
    ],
    "Landroid/os/IMountService$Stub$Proxy;" : [
        ("F","mountMedi","()"),
        ("F","unmountMedi","()"),
    ],
    "Landroid/os/storage/StorageManager;" : [
        ("F","disableUsbMassStorage","()"),
        ("F","enableUsbMassStorage","()"),
    ],
},

"com.android.launcher3.permission.PRELOAD_WORKSPACE" : {
    "Landroid/content/Intent;" : [
        ("C","com.android.launcher3.action.PRELOAD_WORKSPACE","null"),
    ],
},

"BACKUP" : {
    "Landroid/app/backup/BackupManager;" : [
        ("F","beginRestoreSession","()"),
        ("F","dataChanged","(Ljava/lang/String;)"),
        ("F","requestRestore","(Landroid/app/backup/RestoreObserver;)"),
    ],
    "Landroid/app/backup/IBackupManager$Stub$Proxy;" : [
        ("F","backupNow","()"),
        ("F","beginRestoreSession","(Ljava/lang/String;)"),
        ("F","clearBackupData","(Ljava/lang/String;)"),
        ("F","dataChanged","(Ljava/lang/String;)"),
        ("F","getCurrentTransport","()"),
        ("F","isBackupEnabled","()"),
        ("F","listAllTransports","()"),
        ("F","selectBackupTransport","(Ljava/lang/String;)"),
        ("F","setAutoRestore","(B)"),
        ("F","setBackupEnabled","(B)"),
    ],
    "Landroid/app/IActivityManager$Stub$Proxy;" : [
        ("F","bindBackupAgent","(Landroid/content/pm/ApplicationInfo; I)"),
    ],
},

"android.permission.MASTER_CLEAR" : {
    "Landroid/content/Intent;" : [
        ("C","android.intent.action.MASTER_CLEAR com.google.android.c2dm.intent.RECEIVE","null"),
    ],
},

}