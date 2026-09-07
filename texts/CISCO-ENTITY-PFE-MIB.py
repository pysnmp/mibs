#
# PySNMP MIB module CISCO-ENTITY-PFE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ENTITY-PFE-MIB
# Source digest sha256:eb517a1e1a04663d74b2245584d0d29a50bf90b8f54294bd489a908571dfd3d1
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
ciscoEntityPfeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 265))
ciscoEntityPfeMib.setRevisions(('2002-11-27 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityPfeMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityPfeMib.setLastUpdated('2002-11-27 16:00')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setOrganization('Cisco System, Inc.')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setContactInfo('Postal: Cisco Systems, Inc.\n        170 West Tasman Drive\n        San Jose, CA 95134-1706\n        USA\n\n        Tel: +1 800 553-NETS\n\n        E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setDescription('The Packet Forwarding Engine technology are Cisco developed \n        Network Processors, which accelerates certain features in \n        order to provide better network performance.\n\n        An agent uses this MIB to monitor the performance history \n        on any active PFE pipeline listed in the ENTITY-MIB (RFC 2737)\n        entPhysicalTable. This monitoring is via measurement periods\n        of actual, 1-minute, 5-minutes and 15-minutes.\n\n        For the 1-minute and 5-minute measurement periods, perfor-\n        mance statistics are calculated and displayed based on pre-\n        vious 1 minute and 5 minute respectively.\n\n        For the 15-minute period, the performance statistics are\n        accumulated in fifteen minute intervals.  At any one time, \n        an agent maintains one current (incomplete) interval and up \n        to 96 completed intervals (24 hours worth).  Fewer than 96 \n        intervals of data will be available if the agent has been \n        restarted within the last 24 hours. In addition, there is a \n        rolling 24-hour total of each performance statistic.\n\n        There is no requirement for an agent to ensure fixed rela-\n        tionship between the start of a fifteen minute interval and \n        any wall clock; however some agents may align the fifteen \n        minute intervals with quarter hours.')
class CurrentUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represent the actual utilization \n        performance measurement.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class CurrentEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the actual efficiency \n        performance measurement.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represents the utilization perfor-\n        mance measurement in a previous 15 minute measurement \n        interval. In the case where the agent has no valid data\n        available for a particular interval the corresponding object \n        instance is not available and upon a retrieval request a \n        corresponding error message shall be returned to indicate \n        that this instance does not exist (for example, a \n        noSuchObject error for SNMPv1 and a noSuchInstance for \n        SNMPv2 GET operation).\n\n        In a system supporting a history of n intervals with \n        IntervalUtilization(1) and IntervalUtilization(n) the most \n        and least recent intervals respectively, the following proce-\n        dure is used to update the intervals at end of a 15 minute \n        interval:\n           - discard the value of IntervalUtilization(n)\n           - the value of IntervalUtilization(i) becomes that\n             of IntervalUtilization(i-1) for n >= i > 1\n           - the value of IntervalUtilization(1) becomes that\n             of current 15-minute %utilization.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the efficiency\n        performance measurement in a previous 15 minute measurement \n        interval. In the case where the agent has no valid data\n        available for a particular interval the corresponding object \n        instance is not available and upon a retrieval request a \n        corresponding error message shall be returned to indicate \n        that this instance does not exist (for example, a \n        noSuchObject error for SNMPv1 and a noSuchInstance for \n        SNMPv2 GET operation).\n\n        In a system supporting a history of n intervals with \n        IntervalEfficiency(1) and IntervalEfficiency(n) the most and \n        least recent intervals respectively, the following procedure \n        is used to update the intervals at end of a 15 minute inter-\n        val:\n           - discard the value of IntervalEfficiency(n)\n           - the value of IntervalEfficiency(i) becomes that\n             of IntervalEfficiency(i-1) for n >= i > 1\n           - the value of IntervalEfficiency(1) becomes that\n             of currente 15-minute %efficiency.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represents the total running utili-\n        zation performance measurements.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the total running Effi-\n        ciency performance measurements.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class Percentage(TextualConvention, Unsigned32):
    description = 'A percentage value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class EventType(TextualConvention, Integer32):
    description = "Type of action to execute when an event occurs.\n\n       'none'     Neither log an entry in the cePfeHistTable, nor  \n                  sent out an SNMP notification.\n\n       'log'      Create a cePfeHistTable entry, but do not sent out\n                  an SNMP notification.\n\n       'notify'   Sent out an SNMP notification, but do not create a \n                  log entry in the cePfeHistTable.\n\n       'logAndNotify' Both create a log entry in the cePfeHistTable \n                      and sent out an SNMP notification."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("log", 2), ("notify", 3), ("logAndNotify", 4))

class HistEventType(TextualConvention, Integer32):
    description = "Type of event that has occurred.\n\n        'thldUtilizationEvent'\n                   This event is generated if the\n                   cePfePerfCurrentUtilization, at the time of \n                   sampling, becomes greater than or equal to the \n                   cePfePerfThldUtilization.\n\n        'thldEfficiencyEvent'\n                   This event is generated if the \n                   cePfePerfCurrentEfficiency, at the time of \n                   sampling, becomes less than or equal to the \n                   cePfePerfThldEfficiency.\n\n        'thld1MinUtilizationEvent'\n                   This event is generated if the \n                   cePfePerfCurrent1MinUtilization, at the time of \n                   sampling, becomes greater than or equal to the \n                   cePfePerfThld1MinUtilization.\n\n        'thld1MinEfficiencyEvent'\n                   This event is generated if the \n                   cePfePerfCurrent1MinEfficiency, at the time of \n                   sampling, becomes less than or equal to the \n                   cePfePerfThld1MinEfficiency.\n\n        'thld5MinUtilizationEvent'\n                   This event is generated if the \n                   cePfePerfCurrent5MinUtilization, at the time of \n                   sampling, becomes greater than or equal to the \n                   cePfePerfThld5MinUtilization.\n\n        'thld5MinEfficiencyEvent'\n                   This event is generated if the \n                   cePfePerfCurrent5MinEfficiency, at the time of \n                   sampling, becomes less than or equal to the \n                   cePfePerfThld5MinEfficiency.\n\n        'restartEvent'\n                  This event is generated every time the processor \n                  gets restarted."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("thldUtilizationEvent", 1), ("thldEfficiencyEvent", 2), ("thld1MinUtilizationEvent", 3), ("thld1MinEfficiencyEvent", 4), ("thld5MinUtilizationEvent", 5), ("thld5MinEfficiencyEvent", 6), ("restartEvent", 7))

cePfeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 0))
cePfeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1))
cePfeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2))
cePfePerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1))
cePfeHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2))
cePfePerfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfePerfConfigTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigTable.setDescription('This table contains configuration information on a PFE \n        pipeline.')
cePfePerfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigEntry.setDescription('An entry will exist for each entry in the entPhysicalTable \n        that correspond to an active PFE pipeline.')
cePfePerfConfigTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigTimeElapsed.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigTimeElapsed.setDescription("The number of seconds that have elapsed since the beginning \n        of the current 15 min interval. If for some reason, such as \n        an adjustment in the system's time-of-day clock, the current \n        interval exceeds the maximum value, the agent will return the\n        maximum value.")
cePfePerfConfigValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigValidIntervals.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigValidIntervals.setDescription('The number of completed 15 min intervals for which valid \n        PFE performance data has been collected. The value \n        will be 96 unless the interface was brought online within the\n        last 24 hours, in which case the value will be the number of \n        completed 15 minute intervals since the PFE pipeline has \n        been online.')
cePfePerfConfigThldUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 3), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThldUtilization.setDescription("This object contains the threshold value for the \n        cePfePerfCurrentUtilization object. If during the last 5\n        second measurement period the cePfePerfCurrentUtilization\n        object becomes greater than or equal to this threshold value,\n        an event of type 'thldUtilizationEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrentUtilization object value and\n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfConfigThldEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 4), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThldEfficiency.setDescription("This object contains the threshold value for the \n        cePfePerfCurrentEffciency object. If during the last 5 \n        second measurement period the cePfePerfCurrentEfficiency\n        object becomes less than or equal to this threshold value,\n        an event of type 'thldEfficiencyEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrentEfficiency object value and \n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfConfigThld1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 5), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld1MinUtilization.setDescription("This object contains the threshold value for the \n        cePfePerfCurrent1MinUtilization object. If during the last 1\n        minute measurement period the cePfePerfCurrent1MinUtilization\n        object becomes greater than or equal to this threshold value,\n        an event of type 'thld1MinUtilizationEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrent1MinUtilization object value and\n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfConfigThld1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 6), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld1MinEfficiency.setDescription("This object contains the threshold value for the \n        cePfePerfCurrent1MinEfficiency object. If during the last 1 \n        minute measurement period the cePfePerfCurrent1MinEfficiency\n        object becomes less than or equal to this threshold value,\n        an event of type 'thld1MinEfficiencyEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrent1MinEfficiency object value and \n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfConfigThld5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 7), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld5MinUtilization.setDescription("This object contains the threshold value for the \n        cePfePerfCurrent5MinUtilization object. If during the last 5\n        minute measurement period the cePfePerfCurrent5MinUtilization\n        object becomes greater than or equal to this threshold value,\n        an event of type 'thld5MinUtilizationEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrent5MinUtilization object value and\n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfConfigThld5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 8), Percentage().clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld5MinEfficiency.setDescription("This object contains the threshold value for the \n        cePfePerfCurrent5MinEfficiency object. If during the last 5 \n        minute measurement period the cePfePerfCurrent5MinEfficiency\n        object becomes less than or equal to this threshold value,\n        an event of type 'thld5MinEfficiencyEvent' will be genera-\n        ted.\n\n        Value of zero indicates that no comparison is being made\n        between the cePfePerfCurrent5MinEfficiency object value and \n        the threshold value, therefore no event action will be gene-\n        rated.")
cePfePerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfePerfCurrentTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentTable.setDescription('This table maintains PFE current running performance, which \n        are collected at various measurement periods.')
cePfePerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1), ).setMaxAccess("notaccessible")
cePfePerfConfigEntry.registerAugmentions(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEntry"))
cePfePerfCurrentEntry.setIndexNames(*cePfePerfConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cePfePerfCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentEntry.setDescription('An entry containing performance information applicable to\n        a particular PFE pipeline.')
cePfePerfCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 1), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentUtilization.setDescription('This object provides the actual PFE percentage utilization. \n        It is determined by the number of new work contexts + feedback\n        contexts divided by total number of contexts that can be \n        supported by the PFE pipeline.')
cePfePerfCurrentEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 2), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentEfficiency.setDescription('This object provides the actual PFE percentage efficiency. \n        It is determined by the total number of contexts per second \n        divided by maximum theoretical contexts per second supported \n        by the PFE pipeline. Under normal conditions, this number will \n        be 100 and when efficiency starts degrading, it will start \n        going down until it reaches zero.')
cePfePerfCurrent1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 3), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent1MinUtilization.setDescription('This object provides the PFE percentage utilization over the \n        previous 1 minute period. It is determined by the number of new\n        work contexts + feedback contexts divided by total number of \n        contexts that can be supported by the PFE pipeline.')
cePfePerfCurrent1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 4), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent1MinEfficiency.setDescription('This object provides the PFE percentage efficiency over the\n        previous 1 minute period. It is determined by the totalnumber\n        of contexts per second divided by maximum theoretical contexts \n        per second supported by the PFE pipeline. Under normal \n        conditions, this number will be 100 and when efficiency starts \n        degrading, it will start going down until it reaches zero.')
cePfePerfCurrent5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 5), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent5MinUtilization.setDescription('This object provides the PFE percentage utilization over the \n        previous 5 minutes period. It is determined by the number of \n        new work contexts + feedback contexts divided by total number \n        of contexts that can be supported by the PFE pipeline.')
cePfePerfCurrent5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 6), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent5MinEfficiency.setDescription('This object provides the PFE percentage efficiency over the \n        previous 5 minutes period. It is determined by the total number\n        of contexts per second divided by maximum theoretical contexts \n        per second supported by the PFE pipeline. Under normal \n        conditions, this number will be 100 and when efficiency starts \n        degrading, it will start going down until it reaches zero.')
cePfePerfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfePerfIntervalTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalTable.setDescription('This table contains performance statistics for completed \n        15 minutes intervals, specifically up to 96 such intervals\n        over a 24 hours of operation.')
cePfePerfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalNumber"))
if mibBuilder.loadTexts: cePfePerfIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalEntry.setDescription('An entry containing performance information applicable to\n        a particular PFE pipeline at a specific interval.')
cePfePerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfePerfIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalNumber.setDescription('An interval number between 1 and 96, where 1 is the most \n        recently completed 15 min interval and 96 is the 15 min \n        interval completed 23 hours and 45 minutes prior to interval \n        1.')
cePfePerfIntervalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 2), IntervalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalUtilization.setDescription('The percentage of processor utilization by the PFE pipeline\n        during this completed 15 min interval.')
cePfePerfIntervalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 3), IntervalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalEfficiency.setDescription('The percentage of processor efficiency by the PFE pipeline\n        during this completed 15 min interval. Under normal conditions,\n        this number will be 100 and when efficiency starts degrading,\n        it will start going down until it reaches zero.')
cePfePerfTotalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfePerfTotalTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalTable.setDescription('This table contains the running utilization and efficiency \n        of the PFE pipeline for the 24 hour period preceding the \n        current interval. If the agent was restarted less than 24\n        hours ago, i.e., when there are less than 96 intervals in the\n        cePfePerfIntervalTable, it will contain the running utiliza-\n        tion and efficiency up to the last collected 15 minute inter-\n        val.')
cePfePerfTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfTotalEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalEntry.setDescription('An entry containing performance information applicable to\n        a particular PFE pipeline at the end of each interval in the\n        cePfePerfIntervalTable.')
cePfePerfTotalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 1), TotalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalUtilization.setDescription('The running utilization by the PFE pipeline for the prece-\n        ding 24 hrs.')
cePfePerfTotalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 2), TotalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalEfficiency.setDescription('The running efficiency by the PFE pipeline for the preceding\n        24 hrs. Under normal conditions, this number will be 100 and \n        when efficiency starts degrading, it will start going down\n        until it reaches zero.')
cePfeHistNotifiesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 1), EventType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistNotifiesEnable.setStatus('current')
if mibBuilder.loadTexts: cePfeHistNotifiesEnable.setDescription('This object indicates what type of action should be taken by\n        the agent when a event is generated.')
cePfeHistTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500)).clone(0)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistTableSize.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTableSize.setDescription("This object specifies the number of entries that the \n        cePfeHistTable can contain.  When a event is generated, and \n        the capacity of the cePfeHistTable has reached the value \n        specified by this object, then the agent deletes the oldest \n        entity in order to accommodate the new entry. A value of '0' \n        prevents any history from being retained.")
cePfeHistTableLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(0)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTableLastIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTableLastIndex.setDescription('This object specifies the value of the cePfeHistIndex object\n        corresponding to the last entry added to the table by the \n        agent. It will return zero if there are no entries in the\n        table.\n\n        If the management client uses the notifications defined by \n        this module, then it can poll this object to determine \n        whether it has missed a notification sent by the agent.')
cePfeHistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfeHistTable.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTable.setDescription('This table contains a history of events generated by the \n        agent.')
cePfeHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ENTITY-PFE-MIB", "cePfeHistIndex"))
if mibBuilder.loadTexts: cePfeHistEntry.setStatus('current')
if mibBuilder.loadTexts: cePfeHistEntry.setDescription("An entry will exist for each event that has occured while \n        cePfeHistNotifiesEnable object is set to 'log(2)' or \n        'logAndNotify(4)'.")
cePfeHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: cePfeHistIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistIndex.setDescription("An integer value uniquely identifying the entry in the table. \n        The value of this object starts at '1' and monotonically\n        increases for each event condition transition monitored by the\n        agent.  If the value of this object is '4294967295', the agent \n        will reset the index to '1' upon monitoring the next event \n        condition transition.")
cePfeHistEntPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistEntPhysIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistEntPhysIndex.setDescription('The value in this object is equal to the value of the \n        entPhysicalIndex, from the Physical Entity Table (RFC 2037),\n        that is associated with the PFE pipeline that has caused \n        this event.')
cePfeHistType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 3), HistEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistType.setStatus('current')
if mibBuilder.loadTexts: cePfeHistType.setDescription('This object describes the type of event that has occurred.')
cePfeHistThld = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 4), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistThld.setStatus('current')
if mibBuilder.loadTexts: cePfeHistThld.setDescription('The configured value of the specific threshold.')
cePfeHistValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistValue.setStatus('current')
if mibBuilder.loadTexts: cePfeHistValue.setDescription('The actual value of the specific performance objects, at the\n        time of the sample, which is related to the threshold event.')
cePfeHistRestartReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistRestartReason.setStatus('current')
if mibBuilder.loadTexts: cePfeHistRestartReason.setDescription('The reason for which the PFE pipeline has restarted.')
cePfeHistTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTimeStamp.setDescription('This object specifies the value of the sysUpTime object at\n        the time the event was generated.')
cePfeHistThldEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"))
if mibBuilder.loadTexts: cePfeHistThldEvent.setStatus('current')
if mibBuilder.loadTexts: cePfeHistThldEvent.setDescription("This notification is generated when a threshold event has\n        occurred and the cePfeHistNotifiesEnable is set to \n        'notify (3)' or 'logAndNotify(4)'.\n\n        After generating this notification, another such notifica-\n        tion will not be sent out until the sample value has fallen \n        below the threshold value.")
cePfeHistRestartEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"))
if mibBuilder.loadTexts: cePfeHistRestartEvent.setStatus('current')
if mibBuilder.loadTexts: cePfeHistRestartEvent.setDescription("This notification is generated when a restart event has\n        occurred and the cePfeHistNotifiesEnable is set to \n        'notifyp (3)' or 'logAndNotify(4)'.")
cePfeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1))
cePfeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2))
cePfeMIBPerformanceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeMIBPerformanceGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBCurrentGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistEventGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBIntervalGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBTotalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceCompliance = cePfeMIBPerformanceCompliance.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBPerformanceCompliance.setDescription('An Entity-MIB implementation can implement this module to\n        provide PFE pipeline performance history.')
cePfeMIBPerformanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistTableSize"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTableLastIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistNotifiesEnable"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigTimeElapsed"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigValidIntervals"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceGroup = cePfeMIBPerformanceGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBPerformanceGroup.setDescription('The collection of objects which are used to manage the per-\n        formance history of the PFE pipeline.')
cePfeMIBCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBCurrentGroup = cePfeMIBCurrentGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBCurrentGroup.setDescription("The collection of objects which are used to maintain the PFE\n        processor's performance history over a 24 hour of operation.")
cePfeMIBIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 3)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBIntervalGroup = cePfeMIBIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBIntervalGroup.setDescription("The collection of objects which are used to maintain the PFE\n        processor's performance history over a 24 hour of operation.")
cePfeMIBTotalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 4)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBTotalGroup = cePfeMIBTotalGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBTotalGroup.setDescription('The collection of objects which are used to manage the \n        threshold configuration for the PFE pipeline performance.')
cePfeMIBHistGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 5)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistGroup = cePfeMIBHistGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBHistGroup.setDescription('The collection of objects which are used to manage the \n        threshold configuration for the PFE pipeline performance.')
cePfeMIBHistEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 6)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistThldEvent"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistEventGroup = cePfeMIBHistEventGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBHistEventGroup.setDescription('The collection of objects which are used to generate a \n        threshold event for the PFE pipeline performance.')
mibBuilder.exportSymbols("CISCO-ENTITY-PFE-MIB", CurrentEfficiency=CurrentEfficiency, CurrentUtilization=CurrentUtilization, EventType=EventType, HistEventType=HistEventType, IntervalEfficiency=IntervalEfficiency, IntervalUtilization=IntervalUtilization, PYSNMP_MODULE_ID=ciscoEntityPfeMib, Percentage=Percentage, TotalEfficiency=TotalEfficiency, TotalUtilization=TotalUtilization, cePfeHistEntPhysIndex=cePfeHistEntPhysIndex, cePfeHistEntry=cePfeHistEntry, cePfeHistIndex=cePfeHistIndex, cePfeHistNotifiesEnable=cePfeHistNotifiesEnable, cePfeHistRestartEvent=cePfeHistRestartEvent, cePfeHistRestartReason=cePfeHistRestartReason, cePfeHistTable=cePfeHistTable, cePfeHistTableLastIndex=cePfeHistTableLastIndex, cePfeHistTableSize=cePfeHistTableSize, cePfeHistThld=cePfeHistThld, cePfeHistThldEvent=cePfeHistThldEvent, cePfeHistTimeStamp=cePfeHistTimeStamp, cePfeHistType=cePfeHistType, cePfeHistValue=cePfeHistValue, cePfeHistory=cePfeHistory, cePfeMIBCompliances=cePfeMIBCompliances, cePfeMIBConformance=cePfeMIBConformance, cePfeMIBCurrentGroup=cePfeMIBCurrentGroup, cePfeMIBGroups=cePfeMIBGroups, cePfeMIBHistEventGroup=cePfeMIBHistEventGroup, cePfeMIBHistGroup=cePfeMIBHistGroup, cePfeMIBIntervalGroup=cePfeMIBIntervalGroup, cePfeMIBNotifications=cePfeMIBNotifications, cePfeMIBObjects=cePfeMIBObjects, cePfeMIBPerformanceCompliance=cePfeMIBPerformanceCompliance, cePfeMIBPerformanceGroup=cePfeMIBPerformanceGroup, cePfeMIBTotalGroup=cePfeMIBTotalGroup, cePfePerfConfigEntry=cePfePerfConfigEntry, cePfePerfConfigTable=cePfePerfConfigTable, cePfePerfConfigThld1MinEfficiency=cePfePerfConfigThld1MinEfficiency, cePfePerfConfigThld1MinUtilization=cePfePerfConfigThld1MinUtilization, cePfePerfConfigThld5MinEfficiency=cePfePerfConfigThld5MinEfficiency, cePfePerfConfigThld5MinUtilization=cePfePerfConfigThld5MinUtilization, cePfePerfConfigThldEfficiency=cePfePerfConfigThldEfficiency, cePfePerfConfigThldUtilization=cePfePerfConfigThldUtilization, cePfePerfConfigTimeElapsed=cePfePerfConfigTimeElapsed, cePfePerfConfigValidIntervals=cePfePerfConfigValidIntervals, cePfePerfCurrent1MinEfficiency=cePfePerfCurrent1MinEfficiency, cePfePerfCurrent1MinUtilization=cePfePerfCurrent1MinUtilization, cePfePerfCurrent5MinEfficiency=cePfePerfCurrent5MinEfficiency, cePfePerfCurrent5MinUtilization=cePfePerfCurrent5MinUtilization, cePfePerfCurrentEfficiency=cePfePerfCurrentEfficiency, cePfePerfCurrentEntry=cePfePerfCurrentEntry, cePfePerfCurrentTable=cePfePerfCurrentTable, cePfePerfCurrentUtilization=cePfePerfCurrentUtilization, cePfePerfIntervalEfficiency=cePfePerfIntervalEfficiency, cePfePerfIntervalEntry=cePfePerfIntervalEntry, cePfePerfIntervalNumber=cePfePerfIntervalNumber, cePfePerfIntervalTable=cePfePerfIntervalTable, cePfePerfIntervalUtilization=cePfePerfIntervalUtilization, cePfePerfTotalEfficiency=cePfePerfTotalEfficiency, cePfePerfTotalEntry=cePfePerfTotalEntry, cePfePerfTotalTable=cePfePerfTotalTable, cePfePerfTotalUtilization=cePfePerfTotalUtilization, cePfePerformance=cePfePerformance, ciscoEntityPfeMib=ciscoEntityPfeMib)
