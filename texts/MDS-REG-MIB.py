#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 09:03:46 2023
# On host fv-az1032-268 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, Counter32, NotificationType, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, iso, IpAddress, TimeTicks, Integer32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "iso", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MDS-REG-MIB", mdsPointToPoint=mdsPointToPoint, mdsWideband=mdsWideband, mdsSoftware=mdsSoftware, mdsRoot=mdsRoot, mdsGlobalRegModule=mdsGlobalRegModule, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsBroadband=mdsBroadband, PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsNarrowband=mdsNarrowband)
