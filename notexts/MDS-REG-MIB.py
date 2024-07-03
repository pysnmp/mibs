#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:23:08 2024
# On host fv-az1022-995 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, enterprises, Integer32, NotificationType, Gauge32, Counter64, TimeTicks, Unsigned32, iso, IpAddress, ObjectIdentity, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "enterprises", "Integer32", "NotificationType", "Gauge32", "Counter64", "TimeTicks", "Unsigned32", "iso", "IpAddress", "ObjectIdentity", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdsGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 4))
mdsGlobalRegModule.setRevisions(('2006-02-08 00:00',))
if mibBuilder.loadTexts: mdsGlobalRegModule.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: mdsGlobalRegModule.setOrganization('Microwave Data Systems, Inc.')
mdsRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130))
if mibBuilder.loadTexts: mdsRoot.setStatus('current')
mdsWideband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1))
if mibBuilder.loadTexts: mdsWideband.setStatus('current')
mdsPointToPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1, 1))
if mibBuilder.loadTexts: mdsPointToPoint.setStatus('current')
mdsNarrowband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2))
if mibBuilder.loadTexts: mdsNarrowband.setStatus('current')
mdsPointToMultiPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2, 1))
if mibBuilder.loadTexts: mdsPointToMultiPoint.setStatus('current')
mdsBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 3))
if mibBuilder.loadTexts: mdsBroadband.setStatus('current')
mdsSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 9))
if mibBuilder.loadTexts: mdsSoftware.setStatus('current')
mibBuilder.exportSymbols("MDS-REG-MIB", mdsBroadband=mdsBroadband, mdsNarrowband=mdsNarrowband, mdsSoftware=mdsSoftware, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsPointToPoint=mdsPointToPoint, mdsGlobalRegModule=mdsGlobalRegModule, mdsWideband=mdsWideband, PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsRoot=mdsRoot)
