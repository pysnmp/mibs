#
# PySNMP MIB module ACMEPACKET-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oracle/ACMEPACKET-TC
# Produced by pysmi-1.1.12 at Mon Jun  3 13:11:57 2024
# On host fv-az1121-719 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
acmepacket, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacket")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Bits, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Unsigned32, ObjectIdentity, Counter64, MibIdentifier, Gauge32, ModuleIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Unsigned32", "ObjectIdentity", "Counter64", "MibIdentifier", "Gauge32", "ModuleIdentity", "IpAddress", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
apTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 0))
apTextualConventions.setRevisions(('2012-02-06 23:05', '2012-05-05 23:05', '2014-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apTextualConventions.setRevisionsDescriptions(('Initial revision.', 'Expanded ApHardwareModuleFamily with niu10g.', 'Updated Organization and Contact info.',))
if mibBuilder.loadTexts: apTextualConventions.setLastUpdated('201406260000Z')
if mibBuilder.loadTexts: apTextualConventions.setOrganization('Oracle Communications')
if mibBuilder.loadTexts: apTextualConventions.setContactInfo('           \tCustomer Service\n\t\t \tPostal:\t\tOracle Communications\n\t\t\t\t\t100 Crosby Drive \n\t\t\t\t\tBedford, MA 01730\n\t\t\t\t\tUS\n\t\t    \tTel:\t\t1-800-633-0738\n\t\t\tUrl:\t\twww.oracle.com\n\t\t \tE-mail:\t\tsupport@oracle.com')
if mibBuilder.loadTexts: apTextualConventions.setDescription('This module contains common textual convention\n                     definitons used by various Acme Packet MIB modules.')
class ApHardwareModuleFamily(TextualConvention, Integer32):
    description = 'The hardware module types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 17, 18, 19, 24, 25, 26, 240, 241, 242))
    namedValues = NamedValues(("unknown", 0), ("spu", 17), ("npu", 18), ("tcu", 19), ("niuCopper", 24), ("niuFiber", 25), ("miu", 26), ("fanTray", 240), ("powerSupply", 241), ("niu10g", 242))

class ApRedundancyState(TextualConvention, Integer32):
    description = 'The redundancy states that system or card can be in.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("unknown", 0), ("initial", 1), ("active", 2), ("standby", 3), ("outOfService", 4), ("unassigned", 5), ("activePending", 6), ("standbyPending", 7), ("outOfServicePending", 8), ("recovery", 9))

class ApPhyPortType(TextualConvention, Integer32):
    description = 'The physical port type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("unknown", 0), ("sfp", 1))

class ApPresence(TextualConvention, Integer32):
    description = 'The Presence of the physical entity.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("inserted", 1), ("removed", 2))

class ApTransportType(TextualConvention, Integer32):
    description = 'The transport type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("tcp", 1), ("sctp", 2))

class ApServerStatus(TextualConvention, Integer32):
    description = 'The server status .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("inservice", 0), ("lowerpriority", 1), ("oosunreachable", 2))

class ApDiamResultCode(TextualConvention, Integer32):
    description = 'The Result-Code AVP (268) value \n               RFC 3588, 7.1. Result-Code AVP'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1001, 2001, 2002, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 4001, 4002, 4003, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009, 5010, 5011, 5012, 5013, 5014, 5015, 5016, 5017))
    namedValues = NamedValues(("diameterMultiRoundAuth", 1001), ("diameterSuccess", 2001), ("diameterLimitedSuccess", 2002), ("diameterCommandUnsupported", 3001), ("diameterUnableToDeliver", 3002), ("diameterRealmNotServed", 3003), ("diameterTooBusy", 3004), ("diameterLoopDetected", 3005), ("diameterRedirectIndicatoion", 3006), ("diameterApplicationUnsupported", 3007), ("diameterInvalidHdrBits", 3008), ("diameterInvalidAvpBits", 3009), ("diameterUnknownPeer", 3010), ("diameterAuthenticationRejected", 4001), ("diameterOutOfSpace", 4002), ("electionLost", 4003), ("diameterAvpUnsupported", 5001), ("diameterUnknownSessionId", 5002), ("diameterAuthoriszationRejected", 5003), ("diameterInvalidAvpValue", 5004), ("diameterMissingAvp", 5005), ("diameterResourcesExceeded", 5006), ("diameterContradictingAvps", 5007), ("diameterAvpNotAllowed", 5008), ("diameterAvpTooManyTimes", 5009), ("diameterNoCommonApplication", 5010), ("diameterUnsupportedVersion", 5011), ("diameterUnableToComply", 5012), ("diameterInvalidBitInHeader", 5013), ("diameterInvalidAvpLength", 5014), ("diameterInvalidMessageLength", 5015), ("diameterInvalidAvpBitCombo", 5016), ("diameterNoCommonSecurity", 5017))

class ApPercentage(TextualConvention, Integer32):
    description = 'This value is percentage. For example, if the value from \n\t\tGETs is 15, which means 15%, or 0.15.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class ApSipMethod(TextualConvention, Integer32):
    description = 'The SIP message method'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("other", 1), ("invite", 2), ("ack", 3), ("bye", 4), ("register", 5), ("cancel", 6), ("prack", 7), ("options", 8), ("info", 9), ("subscribe", 10), ("notify", 11), ("refer", 12), ("update", 13), ("message", 14), ("publish", 15))

class ApThreadOverloaded(TextualConvention, Integer32):
    description = 'Data type for thread overload'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notApplicable", 1), ("true", 2), ("false", 3))

class ApCommMonitorState(TextualConvention, Integer32):
    description = 'The commMonitor state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("outofservice", 0), ("connecting", 1), ("connected", 2), ("inservice", 3))

class ApAclType(TextualConvention, Integer32):
    description = 'The acl type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("untrusted", 0), ("trusted", 1))

mibBuilder.exportSymbols("ACMEPACKET-TC", ApTransportType=ApTransportType, ApAclType=ApAclType, ApHardwareModuleFamily=ApHardwareModuleFamily, ApPhyPortType=ApPhyPortType, ApDiamResultCode=ApDiamResultCode, ApServerStatus=ApServerStatus, ApThreadOverloaded=ApThreadOverloaded, ApPercentage=ApPercentage, PYSNMP_MODULE_ID=apTextualConventions, ApSipMethod=ApSipMethod, apTextualConventions=apTextualConventions, ApRedundancyState=ApRedundancyState, ApCommMonitorState=ApCommMonitorState, ApPresence=ApPresence)
