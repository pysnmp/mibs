#
# PySNMP MIB module MY-TC (http://snmplabs.com/pysmi)
# ASN.1 source MY-TC
# Source digest sha256:5ada24cfb2e5100f0645a43561b30e62508e7b5afae9de037c6767ad12d6c7e4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
myModules, = mibBuilder.importSymbols("MY-SMI", "myModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
myTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 4, 1))
myTextualConventions.setRevisions(('2002-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: myTextualConventions.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: myTextualConventions.setLastUpdated('2002-03-20 00:00')
if mibBuilder.loadTexts: myTextualConventions.setOrganization('$Company$')
if mibBuilder.loadTexts: myTextualConventions.setContactInfo(' \n                Tel: $Telephone$ \n\n                E-mail: $E-mail$')
if mibBuilder.loadTexts: myTextualConventions.setDescription('This module defines textual conventions used throughout\n                 my enterprise mibs.')
class IfIndex(TextualConvention, Integer32):
    description = 'This textual convention is an extension of the interface \n                index convention. Interface include physical port and\n                aggreate port and switch virtual interface and \n                loopBack interface,etc.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MyTrapType(TextualConvention, Integer32):
    description = 'Private trap(event) type of my switch. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("coldMy", 1), ("warmMy", 2), ("linkDown", 3), ("linkUp", 4), ("authenFailure", 5), ("newRoot", 6), ("topoChange", 7), ("hardChangeDetected", 8), ("portSecurityViolate", 9), ("stormAlarm", 10), ("macNotification", 11), ("vrrpNewMaster", 12), ("vrrpAuthFailure", 13), ("powerStateChange", 14), ("fanStateChange", 15), ("ospf", 16), ("pim", 17), ("igmp", 18), ("dvmrp", 19), ("entity", 20), ("cluster", 21), ("temperatureWarning", 22), ("sysGuard", 23), ("bgp", 24), ("lineDetect", 25), ("bgpReachMaxPrefix", 26), ("hardwareNotSupport", 27))

class ConfigStatus(TextualConvention, Integer32):
    description = "Represents the operational status of an table entry.\n        valid(1) -\n              Indicates this entry's status is valid and active. \n        invalid(2) -\n              Indicates this entry's status is invalid. It is decided by\n              implementatio whether entry is delete"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("valid", 1), ("invalid", 2))

class MemberMap(TextualConvention, OctetString):
    description = 'Each octet indicate a Logic port, and each octect can have \n        their content means. The lenth of octet string will change along \n        with change of product.'
    status = 'current'

mibBuilder.exportSymbols("MY-TC", ConfigStatus=ConfigStatus, IfIndex=IfIndex, MemberMap=MemberMap, MyTrapType=MyTrapType, PYSNMP_MODULE_ID=myTextualConventions, myTextualConventions=myTextualConventions)
