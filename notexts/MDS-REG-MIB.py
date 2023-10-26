#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.8 at Thu Oct 26 12:14:53 2023
# On host fv-az1234-823 platform Linux version 6.2.0-1015-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ModuleIdentity, Counter32, Integer32, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, Bits, TimeTicks, NotificationType, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ModuleIdentity", "Counter32", "Integer32", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "TimeTicks", "NotificationType", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("MDS-REG-MIB", PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsNarrowband=mdsNarrowband, mdsSoftware=mdsSoftware, mdsRoot=mdsRoot, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsBroadband=mdsBroadband, mdsPointToPoint=mdsPointToPoint, mdsWideband=mdsWideband, mdsGlobalRegModule=mdsGlobalRegModule)
