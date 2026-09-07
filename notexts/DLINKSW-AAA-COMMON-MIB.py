#
# PySNMP MIB module DLINKSW-AAA-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source DLINKSW-AAA-COMMON-MIB
# Source digest sha256:99e56a8eae584200100e3c1b6bd4a5c1a03fe476f9c78d544e1c825d314394aa
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
dlinkSwAAACommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150))
dlinkSwAAACommonMIB.setRevisions(('2013-01-17 00:00',))
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setLastUpdated('2013-01-17 00:00')
if mibBuilder.loadTexts: dlinkSwAAACommonMIB.setOrganization('D-Link Corp.')
class DAaaSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("telnet", 1), ("console", 2), ("ssh", 3), ("http", 4))

class DAaaPrivilegeLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 15)

class DAaaMethodListName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class DAaaMethodPriority(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4)

class DAaaMethodName(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

dAaaCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 0))
dAaaMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1))
if mibBuilder.loadTexts: dAaaMIBObjects.setStatus('current')
dAaaCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2))
dAaaCommonObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1))
if mibBuilder.loadTexts: dAaaCommonObjects.setStatus('current')
dAaaNewModelEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 150, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dAaaNewModelEnabled.setStatus('current')
dAaaCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1))
daaaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 1, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "daaaGlobalCtrlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaMIBCompliance = daaaMIBCompliance.setStatus('current')
dAaaCommonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2))
daaaGlobalCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 150, 2, 2, 1)).setObjects(("DLINKSW-AAA-COMMON-MIB", "dAaaNewModelEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    daaaGlobalCtrlGroup = daaaGlobalCtrlGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-AAA-COMMON-MIB", DAaaMethodListName=DAaaMethodListName, DAaaMethodName=DAaaMethodName, DAaaMethodPriority=DAaaMethodPriority, DAaaPrivilegeLevel=DAaaPrivilegeLevel, DAaaSessionType=DAaaSessionType, PYSNMP_MODULE_ID=dlinkSwAAACommonMIB, dAaaCommonMIBCompliances=dAaaCommonMIBCompliances, dAaaCommonMIBConformance=dAaaCommonMIBConformance, dAaaCommonMIBGroups=dAaaCommonMIBGroups, dAaaCommonMIBNotifications=dAaaCommonMIBNotifications, dAaaCommonObjects=dAaaCommonObjects, dAaaMIBObjects=dAaaMIBObjects, dAaaNewModelEnabled=dAaaNewModelEnabled, daaaGlobalCtrlGroup=daaaGlobalCtrlGroup, daaaMIBCompliance=daaaMIBCompliance, dlinkSwAAACommonMIB=dlinkSwAAACommonMIB)
