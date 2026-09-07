#
# PySNMP MIB module CISCO-FLOW-MONITOR-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-FLOW-MONITOR-TC-MIB
# Source digest sha256:8e87cd55eca49c31536473f4f2d8edf4c1a94e47a269924ac6752b5bacdd1f16
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlowMonitorTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 688))
ciscoFlowMonitorTcMIB.setRevisions(('2008-12-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setRevisionsDescriptions(('The initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setLastUpdated('2008-12-09 00:00')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA 95134\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setDescription("This MIB module defines textual conventions used by the MIB\n        modules defining objects describing flow monitoring.\n\n        GLOSSARY\n        ============\n\n        Alarm Action - a method used by the device to signal changes in\n            an alarm condition.\n\n        Alarm Aggregation - a technique used to efficiently monitor the\n            same standing condition for a flow set.\n\n        Alarm Condition - a standing condition for which the device\n            signals changes in state.\n\n        Alarm Group - a flow set for which the device monitors a\n            configured standing condition, raising an alarm when a\n            configured number of flows in the flow set assert the\n            standing standing.\n\n        Alarm Severity - the relative disposition of an alarm condition\n            when raised by the device.  For example, a provider may\n            regard a flow stop alarm as having a higher severity than a\n            flow's loss fraction exceeding a configured threshold.\n\n        Flow Monitor - a hardware or software entity that classifies\n            traffic flows, collects flow data, and periodically\n            computes flow metrics.\n\n        Flow Metric - a measurement that reflects the quality of a\n            traffic flow.\n\n        Flow Point - represents the ingress or egress of a traffic flow.\n\n        Flow Set - a group of traffic flows.\n\n        Measurement Interval - the length of time over which a flow\n            monitor collects data related to a traffic flow, after which\n            the flow monitor computes flow metrics using the collected\n            data.\n\n        Standing Condition - represents a lasting error, fault, or\n            warning resulting from the application of a set of criteria\n            to the state of an entity, such as a flow monitor or traffic\n            flow.  For example, a flow monitor may assert a standing\n            condition if the number of traffic flows that expire in a\n            meansurement interval exceeds a configured threshold.\n\n        Traffic Flow - a unidirectional stream of packets conforming to\n            a classifier.  For example, packets having a particular \n            source IP address, destination IP address, protocol type,\n            source port number, and destination port number.\n        ")
class FlowMonitorIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value\n        that uniquely identifies a flow monitor.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value\n        that uniquely identifies a traffic flow within the scope of the\n        flow monitor that collects data and periodically computes\n        metrics for the traffic flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowPointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB',\n        RFC-2863, June 2000."
    description = "This textual convention denotes an enumerated integer-value\n        that represents a point at which a flow monitor collects data\n        for a traffic flow:\n\n            'other'\n                The implementation of the MIB module using this textual\n                convention does not recognize the flow point.\n\n            'unknown'\n                The device is unable to ascertain the point at which\n                the flow monitor collects data for the traffic flow.\n\n            'none'\n                There is no point at which the flow monitor collects\n                data for the traffic flow.\n\n            'interface'\n                The flow point is an interface represented by a row in\n                the ifTable (defined by the IF-MIB [RFC2863].\n\n            'dot1qVlan'\n                The flow point is an IEEE 802.1q VLAN represented by a\n                row in the ifTable (defined by the IF-MIB [RFC2863]) and\n                a tag representing the VLAN.\n\n        With the exception of the values 'unknown' and 'none', each\n        definition of a concrete FlowPointType value MUST have a\n        corresponding textual convention for use with the particular\n        type of flow point.\n\n        To support future extensions, a MIB module SHOULD NOT sub-type\n        the FlowPointType textual convention in an object type\n        definition.  However, a compliance statement MAY sub-type it in\n        order to require only a subset of the flow point types for a\n        compliant implementation.\n\n        Implementations must ensure that FlowPointType objects and any\n        dependent objects (e.g., FlowPointIdentifier objects) are\n        consistent.  For example, an implementation must respond with an\n        'inconsistentValue' error if an attempt is made to modify a\n        FlowPointType object without changing the corresponding\n        FlowPointIdentifier object."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4), ("dot1qVlan", 5))

class FlowPointIdentifier(TextualConvention, OctetString):
    description = "This textual convention denotes an octet string-value that\n        identifies a point at which a flow monitor collects data for a\n        traffic flow.\n\n        An implementation MUST ALWAYS interpret a FlowPointIdentifier\n        value within the context of a FlowPointType value.  Every use\n        of the FlowPointIdentifier textual convention requires the\n        specification of a FlowPointType object to provide the context.\n        A MIB module SHOULD logically register the FlowPointType object\n        before the FlowPointIdentifier object(s).\n\n        The value of a FlowPointIdentifier object MUST BE the null\n        string if the value of the FlowPointType object providing the\n        context is 'unknown' or 'none'.\n\n        Implementations must ensure that a FlowPointIdentifier object\n        remains consistent with the FlowPointType object providing the\n        context.  For example, an implementation must respond with an\n        'inconsistentValue' error if an attempt is made to modify a\n        FlowPointIdentifier object without changing the corresponding\n        FlowPointType object."
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowPointInterface(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group\n        MIB',\n        RFC-2863, June 2000."
    description = "This textual convention denotes an octet string-value\n        identifying a row in ifTable (defined by the IF-MIB [RFC2863]).\n\n            Octets  Contents       Encoding\n            =========================================\n            1-4     ifIndex-value  network-byte order\n\n        The corresponding FlowPointType value is 'interface'.\n\n        A MIB module SHOULD NOT directly use this textual convention in\n        defining object, as it restricts flow points to specific type.\n        However, if a MIB module does chose to directly use the textual\n        convention, it MAY chose to do so without a FlowPointType object\n        to define the context, since this textual convention implies the\n        context."
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FlowPointDot1qVlan(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB',\n        RFC-2863, June 2000."
    description = "This textual convention denotes an octet string-value\n        identifying an IEEE 802.1q VLAN.\n\n            Octets  Contents       Encoding\n            =========================================\n            1-4     ifIndex-value  network-byte order\n            5-6     VLAN tag       network-byte order\n\n        The corresponding FlowPointType value is 'dot1qVlan'.\n\n        A MIB module SHOULD NOT directly use this textual convention in\n        defining object, as it restricts flow points to specific type.\n        However, if a MIB module does chose to directly use the textual\n        convention, it MAY chose to do so without a FlowPointType object\n        to define the context, since this textual convention implies the\n        context."
    status = 'current'
    displayHint = '4d,2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class FlowMetrics(TextualConvention, Bits):
    reference = "H. Schulzrinne, S. Casner, R. Fredrick, and V. Jacobson, 'RTP:\n        A Transport Protocol for Real-Time Applications', RFC-3550, July\n        2003.\n\n        J. Welch and J. Clark, 'A Proposed Media Delivery Index\n        (MDI)', RFC-4445, APril 2006."
    description = "This textual convention denotes an enumerated integer-value\n        that represents a set of metrics:\n\n            'mdi'\n                This set of metrics consists of the Media Delivery Index\n                (MDI) [RFC4445]\n\n            'rtp'\n                This set of metrics consists of data similar to that\n                computed and sent by a RTP client in a RTCP receiver\n                report [RFC3550].\n\n            'ipCbr'\n                This set of metrics complements MDI, measuring the\n                notion of Media Rate Variation (MRV)."
    status = 'current'
    namedValues = NamedValues(("mdi", 0), ("rtp", 1), ("ipCbr", 2))

class FlowCfgRateType(TextualConvention, Integer32):
    reference = "J. Welch and J. Clark, 'A Proposed Media Delivery Index (MDI)',\n        RFC-4445, APril 2006."
    description = "This textual convention denotes an enumerated integer-value\n        that represents the media rate used by the flow monitor to\n        compute the delay factor for a traffic flow:\n        \n            'auto'\n                The device automatically determines the media rate.\n\n            'ipPktRate'\n                The device uses a configured media rate expressed as an\n                IP packet rate.\n\n            'ipBitRate'\n                The device uses a configured media rate expressed as an\n                IP packet rate.\n\n            'mediaRate'\n                The device uses a configured media rate expressed as a\n                media bit rate.\n        "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("ipPktRate", 2), ("ipBitRate", 3), ("mediaRate", 4))

class FlowBitRateUnits(TextualConvention, Integer32):
    description = "This textual convention denotes an enumerated integer-value\n        that represents the units used when presenting a bit rate value.\n\n            'bps'\n                The device presents the rate of a traffic flow in bits\n                per second (bps).\n\n            'kbps'\n                The device presents the rate of a traffic flow in Kbps.\n\n            'mbps'\n                The device presents the rate of a traffic flow in Mbps.\n\n            'gbps'\n                The device presents the rate of a traffic flow in Gbps."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("bps", 1), ("kbps", 2), ("mbps", 3), ("gbps", 4))

class FlowMetricScale(TextualConvention, Integer32):
    description = "This textual convention denotes an enumerated integer-value\n        that represents an International System of Units (SI) prefix\n        used as a scaling factor for fixed-point values:\n\n             Prefix     Scale Factor\n            =========================\n             'yocto'    10E-24\n             'zepto'    10E-21\n             'atto'     10E-18\n             'femto'    10E-15\n             'pico'     10E-12\n             'nano'     10E-9\n             'micro'    10E-6\n             'milli'    10E-3\n             'units'    10E0\n             'kilo'     10E3\n             'mega'     10E6\n             'giga'     10E9\n             'tera'     10E12\n             'exa'      10E15\n             'peta'     10E18\n             'zetta'    10E21\n             'yotta'    10E24\n\n        A MIB module may abstract a fixed-point value by defining three\n        objects together:\n\n        1)  A FlowMetricScale object, which indicates the scale of the\n            value.\n\n        2)  A FlowMetricPrecision object, which indicates the precision\n            of the value.  In the case that the value has a fractional\n            portion, this object indicates the number of digits\n            comprising the fractional portion.\n\n        3)  A FlowMetricValue object, which indicates the value before\n            scaling."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class FlowMetricPrecision(TextualConvention, Integer32):
    description = "This textual convention denotes the precision or accuracy of a\n        fixed-point value.\n\n        A MIB module may abstract a fixed-point value by defining three\n        objects together:\n\n        1)  A FlowMetricScale object, which indicates the scale of the\n            value.\n\n        2)  A FlowMetricPrecision object, which indicates the precision\n            of the value.  In the case that the value has a fractional\n            portion, this object indicates the number of digits\n            comprising the fractional portion.\n\n        3)  A FlowMetricValue object, which indicates the value before\n            scaling.\n\n        If an instance of an object of this type has a value in the\n        range of 1 to 9, then it represents the precision of the\n        associated value; that is, the number of decimal places in the\n        fractional part of the associated value.  For example, if the\n        Media Loss Rate (MLR) computed for a traffic flow is 350.9E-6,\n        then the FlowMetricScale object is 'micro', the\n        FlowMetricPrecision object is 1, and the object indicating the\n        value is 3509.\n\n        If an instance of an object of this type has a value in the\n        range of -8 to -1, then it represents the number of accurate\n        digits in the associated value.  For example, if the jitter\n        measured for a traffic flow can range between -100,000 and\n        100,000 microseconds in 10 microsecond increments, with an\n        accuracy of +/- 5 microseconds, the FlowMetricScale object is\n        'micro', the FlowMetricPrecision object is -2, and the object\n        indicating the value has range of -100,000 to 100,000."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-8, -1), ValueRangeConstraint(1, 9), )
class FlowMetricValue(TextualConvention, Integer32):
    description = 'This textual convention denotes the value of a fixed-point\n        value.\n\n        A MIB module may abstract a fixed-point value by defining three\n        objects together:\n\n        1)  A FlowMetricScale object, which indicates the scale of the\n            value.\n\n        2)  A FlowMetricPrecision object, which indicates the precision\n            of the value.  In the case that the value has a fractional\n            portion, this object indicates the number of digits\n            comprising the fractional portion.\n\n        3)  A FlowMetricValue object, which indicates the value before\n            scaling.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class FlowMonitorConditions(TextualConvention, OctetString):
    description = 'This textual convention denotes a octet string-value that\n        represents the standing conditions associated with an entity,\n        such as a flow monitor a traffic flow.\n\n        Each bit in the string corresponds to a single standing\n        condition.  The device should present a description of the\n        standing condition in the cfmConditionTable, which uniquely\n        identifies such a description by the following tuple:\n\n            [cfmConditionProfile, cfmConditionId]\n\n        where cfmConditionProfile uniquely identifies the conditions\n        profile containing the description and cfmConditionId\n        corresponds to the bit position within the string.  The figure\n        below illustrates a representation of the string containing N\n        octets:\n\n        Octet 0             Octet N-1\n        7 6 5 4 3 2 1 0     7 6 5 4 3 2 1 0\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n        |               |...|               |\n        +-+-+-+-+-+-+-+-+   +-+-+-+-+-+-+-+-+\n        | | | | | | | |     | | | | | | | |\n        | | | | | | | |     | | | | | | | +- Condition 8(n-1)\n        | | | | | | | |     | | | | | | +--- Condition 8(n-1)+1\n        | | | | | | | |     | | | | | +----- Condition 8(n-1)+2\n        | | | | | | | |     | | | | +------- Condition 8(n-1)+3\n        | | | | | | | |     | | | +--------- Condition 8(n-1)+4\n        | | | | | | | |     | | +----------- Condition 8(n-1)+5\n        | | | | | | | |     | +------------- Condition 8(n-1)+6\n        | | | | | | | |     +--------------- Condition 8(n-1)+7\n        | | | | | | | |                          :\n        | | | | | | | |                          :\n        | | | | | | | +--------------------- Condition 0\n        | | | | | | +----------------------- Condition 1\n        | | | | | +------------------------- Condition 2\n        | | | | +--------------------------- Condition 3\n        | | | +----------------------------- Condition 4\n        | | +------------------------------- Condition 5\n        | +--------------------------------- Condition 6\n        +----------------------------------- Condition 7'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowMonitorConditionsProfile(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value\n        that uniquely identifies a conditions profile.  A conditions\n        profile is a set of descriptions of standing/alarm conditions\n        that can be applied to an entity, such as a flow alarm or a\n        traffic flow.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowMonitorConditionsProfileOrZero(TextualConvention, Unsigned32):
    description = "This textual convention serves as an extension of the\n        FlowMonitorConditionsProfile textual convention, which permits\n        the value '0'. The use of the value '0' is specific to an\n        object, thus requiring the descriptive text associated with the\n        object to describe the semantics of its use."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class FlowMonitorConditionIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an integer-value representing\n        a standing/alarm condition within a conditions profile.  It has\n        a direct correspondence to the position of the bit representing\n        the standing/alarm condition in a FlowMonitorConditions object.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2039)

class FlowMonitorAlarmGroupIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value\n        that uniquely identifies an alarm group.  An alarm group\n        represents an alarm condition that the device raises if a\n        configured number of traffic flows in a configured set of\n        traffic flows asserts a given standing condition.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowSetIdentifier(TextualConvention, Unsigned32):
    description = 'This textual convention denotes an arbitrary integer-value\n        that uniquely identifies a set of traffic flows.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

mibBuilder.exportSymbols("CISCO-FLOW-MONITOR-TC-MIB", FlowBitRateUnits=FlowBitRateUnits, FlowCfgRateType=FlowCfgRateType, FlowIdentifier=FlowIdentifier, FlowMetricPrecision=FlowMetricPrecision, FlowMetricScale=FlowMetricScale, FlowMetricValue=FlowMetricValue, FlowMetrics=FlowMetrics, FlowMonitorAlarmGroupIdentifier=FlowMonitorAlarmGroupIdentifier, FlowMonitorConditionIdentifier=FlowMonitorConditionIdentifier, FlowMonitorConditions=FlowMonitorConditions, FlowMonitorConditionsProfile=FlowMonitorConditionsProfile, FlowMonitorConditionsProfileOrZero=FlowMonitorConditionsProfileOrZero, FlowMonitorIdentifier=FlowMonitorIdentifier, FlowPointDot1qVlan=FlowPointDot1qVlan, FlowPointIdentifier=FlowPointIdentifier, FlowPointInterface=FlowPointInterface, FlowPointType=FlowPointType, FlowSetIdentifier=FlowSetIdentifier, PYSNMP_MODULE_ID=ciscoFlowMonitorTcMIB, ciscoFlowMonitorTcMIB=ciscoFlowMonitorTcMIB)
