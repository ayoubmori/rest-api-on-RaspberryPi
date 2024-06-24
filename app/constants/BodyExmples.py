addProgramBodyExmple = {
    "controlProgramId": 2456468648,
    "version": 1,
    "name": "Sample Control Program",
    "timeControls": [
        {
            "timeEvtType": "Fixed time",
            "dimmingLevel": 50,
            "fixedTime": "12:00",
            "offset": 30
        }
    ]}
########################
addCalendarBodyExmple = {
    "calendarId": 587585,
    "version": 1,
    "name": "test1 Calendar",
    "defaultCtrProgId": 542274,
    "rules": [
        {
            "ctrProgId": 1001,
            "timeConditiontype": 1,
            "start": "2024-03-12",
            "end": "2024-10-20"
        },
        {
            "ctrProgId": 1002,
            "timeConditiontype": 2,
            "start": "2024-03-12",
            "end": "2024-10-20"
        }
    ],
    "lamp": [
        {"id": "relay1"}
    ]
}

#####################
