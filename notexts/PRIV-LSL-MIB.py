#
# PySNMP MIB module PRIV-LSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-LSL-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:20 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, Gauge32, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, iso, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "Gauge32", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "iso", "NotificationType", "MibIdentifier")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
privLsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 113))
privLsl.setRevisions(('2008-03-21 00:00',))
if mibBuilder.loadTexts: privLsl.setLastUpdated('200803210000Z')
if mibBuilder.loadTexts: privLsl.setOrganization('BATM Advanced Communication')
privLslLevel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1))
privLslObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1))
privLslNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 2))
privLslConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3))
class PrivLslStates(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

privLslGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslGlobalMacAddress.setStatus('current')
privLslManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2), )
if mibBuilder.loadTexts: privLslManagementTable.setStatus('current')
privLslManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privLslManagementEntry.setStatus('current')
privLslStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslStatus.setStatus('current')
privIometrixManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3), )
if mibBuilder.loadTexts: privIometrixManagementTable.setStatus('current')
privIometrixManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privIometrixManagementEntry.setStatus('current')
privIometrixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privIometrixStatus.setStatus('current')
privLslGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1))
privLslCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2))
privLevel1ObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1, 1)).setObjects(("PRIV-LSL-MIB", "privLslGlobalMacAddress"), ("PRIV-LSL-MIB", "privLslStatus"), ("PRIV-LSL-MIB", "privIometrixStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1ObjectsGroup = privLevel1ObjectsGroup.setStatus('current')
privLevel1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2, 1)).setObjects(("PRIV-LSL-MIB", "privLevel1ObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1Compliance = privLevel1Compliance.setStatus('current')
mibBuilder.exportSymbols("PRIV-LSL-MIB", privLevel1Compliance=privLevel1Compliance, privIometrixStatus=privIometrixStatus, privLslGroups=privLslGroups, privLevel1ObjectsGroup=privLevel1ObjectsGroup, privIometrixManagementTable=privIometrixManagementTable, privLslManagementEntry=privLslManagementEntry, privLslStatus=privLslStatus, PrivLslStates=PrivLslStates, privLslLevel1=privLslLevel1, privLslConformance=privLslConformance, privLslManagementTable=privLslManagementTable, privLslNotifications=privLslNotifications, privLslObjects=privLslObjects, privIometrixManagementEntry=privIometrixManagementEntry, privLsl=privLsl, privLslCompliances=privLslCompliances, PYSNMP_MODULE_ID=privLsl, privLslGlobalMacAddress=privLslGlobalMacAddress)
