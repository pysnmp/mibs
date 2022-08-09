#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 15:14:33 2022
# On host fv-az445-955 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, ModuleIdentity, Counter64, Gauge32, Integer32, ObjectIdentity, Counter32, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "ModuleIdentity", "Counter64", "Gauge32", "Integer32", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdsGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 4))
mdsGlobalRegModule.setRevisions(('2006-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsGlobalRegModule.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: mdsGlobalRegModule.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: mdsGlobalRegModule.setOrganization('Microwave Data Systems, Inc.')
if mibBuilder.loadTexts: mdsGlobalRegModule.setContactInfo('Technical Services\n\t\t\t\t\t\t\t\t\t Microwave Data Systems, Inc.\n\t\t\t\t\t\t\t\t \n\t\t\t\t\t\t\t\t\t e-mail: techsupport@microwavedata.com\n\t\t\t\t\t\t\t\t\t phone:(585)241-5510\n\t\t\t\t\t\t\t\t\t fax:(585)242-8369')
if mibBuilder.loadTexts: mdsGlobalRegModule.setDescription('MDS sub-tree registrations')
mdsRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130))
if mibBuilder.loadTexts: mdsRoot.setStatus('current')
if mibBuilder.loadTexts: mdsRoot.setDescription('The root of the OID sub-tree assigned to MDS')
mdsWideband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1))
if mibBuilder.loadTexts: mdsWideband.setStatus('current')
if mibBuilder.loadTexts: mdsWideband.setDescription('Sub-tree for wideband products')
mdsPointToPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1, 1))
if mibBuilder.loadTexts: mdsPointToPoint.setStatus('current')
if mibBuilder.loadTexts: mdsPointToPoint.setDescription('Sub-tree for wideband point-to-point products')
mdsNarrowband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2))
if mibBuilder.loadTexts: mdsNarrowband.setStatus('current')
if mibBuilder.loadTexts: mdsNarrowband.setDescription('Sub-tree for narrowband products')
mdsPointToMultiPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2, 1))
if mibBuilder.loadTexts: mdsPointToMultiPoint.setStatus('current')
if mibBuilder.loadTexts: mdsPointToMultiPoint.setDescription('Sub-tree narrowband point-to-multipoint products')
mdsBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 3))
if mibBuilder.loadTexts: mdsBroadband.setStatus('current')
if mibBuilder.loadTexts: mdsBroadband.setDescription('Sub-tree for broadband products')
mdsSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 9))
if mibBuilder.loadTexts: mdsSoftware.setStatus('current')
if mibBuilder.loadTexts: mdsSoftware.setDescription('Sub-tree for non-equipment software such as desktop applications')
mibBuilder.exportSymbols("MDS-REG-MIB", PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsBroadband=mdsBroadband, mdsPointToPoint=mdsPointToPoint, mdsWideband=mdsWideband, mdsRoot=mdsRoot, mdsNarrowband=mdsNarrowband, mdsGlobalRegModule=mdsGlobalRegModule, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsSoftware=mdsSoftware)
