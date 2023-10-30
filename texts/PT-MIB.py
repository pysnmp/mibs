#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MIB
# Produced by pysmi-1.1.10 at Mon Oct 30 02:17:33 2023
# On host fv-az443-612 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
miniLink, = mibBuilder.importSymbols("MINI-LINK-MIB", "miniLink")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, ObjectIdentity, TimeTicks, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, MibIdentifier, NotificationType, Integer32, iso, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "TimeTicks", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "iso", "ModuleIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2))
pt.setRevisions(('2017-01-21 12:00', '2016-03-09 12:00', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pt.setRevisionsDescriptions(('MOC and MOI explained.', 'Validated.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: pt.setLastUpdated('201701211200Z')
if mibBuilder.loadTexts: pt.setOrganization('Ericsson')
if mibBuilder.loadTexts: pt.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: pt.setDescription('This is the MIB of PT specifics.\n            The entPhysical and ifIndex used are based on the MOC below:\n            IP_INTERFACE_MOC  10000\n            LANX_PORT_MOC     20000\n            WANX_PORT_MOC     30000\n            PT_MOC            40000\n            OM_MOC            50000\n            RMM_MOC           60000\n            SFP_MOC           70000\n            WIFI_MOC          80000\n            RJ45_MOC          90000\n            XPIC_MOC         100000\n            CT_MOC           110000\n            RLT_MOC          120000\n        \n            As MOI, slot and port are added according to:\n            Slot no * 100\n            Port no * 1\n            \n            For example an SFP in slot 1 port 3: 70103')
ptDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptDeviceType.setStatus('current')
if mibBuilder.loadTexts: ptDeviceType.setDescription("This object represents type of the PT. Always set to the\n             same value as 'sysObjectID'.")
ptConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8))
ptCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1))
ptGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2))
ptCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1, 1)).setObjects(("PT-MIB", "ptCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompliance = ptCompliance.setStatus('current')
if mibBuilder.loadTexts: ptCompliance.setDescription('The compliance statement for SNMP entities which implement everything.')
ptCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2, 1)).setObjects(("PT-MIB", "ptDeviceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompleteGroup = ptCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: ptCompleteGroup.setDescription('A collection of all current objects in this MIB module.')
mibBuilder.exportSymbols("PT-MIB", ptCompliances=ptCompliances, ptGroups=ptGroups, ptDeviceType=ptDeviceType, pt=pt, ptCompliance=ptCompliance, ptConformance=ptConformance, PYSNMP_MODULE_ID=pt, ptCompleteGroup=ptCompleteGroup)
