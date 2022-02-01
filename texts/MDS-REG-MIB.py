#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.8 at Tue Feb  1 21:03:38 2022
# On host fv-az121-510 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, NotificationType, Unsigned32, Counter32, IpAddress, Integer32, enterprises, ModuleIdentity, Gauge32, Bits, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "Integer32", "enterprises", "ModuleIdentity", "Gauge32", "Bits", "TimeTicks", "Counter64", "MibIdentifier")
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
mibBuilder.exportSymbols("MDS-REG-MIB", mdsWideband=mdsWideband, PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsNarrowband=mdsNarrowband, mdsPointToPoint=mdsPointToPoint, mdsGlobalRegModule=mdsGlobalRegModule, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsBroadband=mdsBroadband, mdsRoot=mdsRoot, mdsSoftware=mdsSoftware)
