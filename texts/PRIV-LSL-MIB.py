#
# PySNMP MIB module PRIV-LSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-LSL-MIB
# Produced by pysmi-1.1.8 at Thu Jan 13 23:20:39 2022
# On host fv-az83-250 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Counter64, TimeTicks, ModuleIdentity, IpAddress, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Unsigned32, Counter32, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "TimeTicks", "ModuleIdentity", "IpAddress", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Unsigned32", "Counter32", "Bits", "MibIdentifier")
DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress")
privLsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 113))
privLsl.setRevisions(('2008-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: privLsl.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: privLsl.setLastUpdated('200803210000Z')
if mibBuilder.loadTexts: privLsl.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: privLsl.setContactInfo(' BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: privLsl.setDescription('MIB module for management of Logical Service Loopback(LSL) Iometrix compatible product.')
privLslLevel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1))
privLslObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1))
privLslNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 2))
privLslConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3))
class PrivLslStates(TextualConvention, Integer32):
    description = 'The the switch on/off states for LSL on ports.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

privLslGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslGlobalMacAddress.setStatus('current')
if mibBuilder.loadTexts: privLslGlobalMacAddress.setDescription('This object defines the destination mac address assigned\nto lsl packets. The device can recognise the lsl packets\nby a specific destination mac address given by this\nobject.\n')
privLslManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2), )
if mibBuilder.loadTexts: privLslManagementTable.setStatus('current')
if mibBuilder.loadTexts: privLslManagementTable.setDescription('LSL interface extention table.\nThis table contains all objects which are used for LSL\nmanagement per interface. It uses ifIndex defined in\nrfc1213')
privLslManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privLslManagementEntry.setStatus('current')
if mibBuilder.loadTexts: privLslManagementEntry.setDescription('The only valid LSL interfaces are phyical port interfaces')
privLslStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslStatus.setStatus('current')
if mibBuilder.loadTexts: privLslStatus.setDescription('This object indicates whether the port have Logical Service\nLoopback enabled or disabled. It allows the client to\ndetermine which interface should be used for this type\nof service')
privIometrixManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3), )
if mibBuilder.loadTexts: privIometrixManagementTable.setStatus('current')
if mibBuilder.loadTexts: privIometrixManagementTable.setDescription('Iometrix Level 1 table.\nThis table contains all objects which are used for Iometrix\nlevel 1 management per interface. It uses ifIndex defined in\nrfc1213')
privIometrixManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privIometrixManagementEntry.setStatus('current')
if mibBuilder.loadTexts: privIometrixManagementEntry.setDescription('the index is ifindex')
privIometrixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privIometrixStatus.setStatus('current')
if mibBuilder.loadTexts: privIometrixStatus.setDescription('This object indicates whether the port have Logical Service\nLoopback enabled or disabled. It allows the client to\ndetermine which interface should be used for this type\nof service')
privLslGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1))
privLslCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2))
privLevel1ObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1, 1)).setObjects(("PRIV-LSL-MIB", "privLslGlobalMacAddress"), ("PRIV-LSL-MIB", "privLslStatus"), ("PRIV-LSL-MIB", "privIometrixStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1ObjectsGroup = privLevel1ObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: privLevel1ObjectsGroup.setDescription('All objects related to level1 logical loopback service. Object\ngrouping will be extended if the mib is also extended')
privLevel1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2, 1)).setObjects(("PRIV-LSL-MIB", "privLevel1ObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1Compliance = privLevel1Compliance.setStatus('current')
if mibBuilder.loadTexts: privLevel1Compliance.setDescription('The compliance statement. It will be extended if new\nfunctionality is added')
mibBuilder.exportSymbols("PRIV-LSL-MIB", privLslConformance=privLslConformance, privLevel1ObjectsGroup=privLevel1ObjectsGroup, privLevel1Compliance=privLevel1Compliance, privIometrixManagementTable=privIometrixManagementTable, privLslNotifications=privLslNotifications, privLslStatus=privLslStatus, privLslLevel1=privLslLevel1, privLslManagementTable=privLslManagementTable, privIometrixManagementEntry=privIometrixManagementEntry, PYSNMP_MODULE_ID=privLsl, privLslManagementEntry=privLslManagementEntry, privLslObjects=privLslObjects, PrivLslStates=PrivLslStates, privIometrixStatus=privIometrixStatus, privLslGroups=privLslGroups, privLslCompliances=privLslCompliances, privLslGlobalMacAddress=privLslGlobalMacAddress, privLsl=privLsl)
