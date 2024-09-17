#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.12 at Tue Sep 17 12:57:33 2024
# On host fv-az1215-438 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, TimeTicks, iso, Counter64, enterprises, ObjectIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, NotificationType, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "TimeTicks", "iso", "Counter64", "enterprises", "ObjectIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "NotificationType", "Integer32", "Bits")
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
mibBuilder.exportSymbols("MDS-REG-MIB", mdsWideband=mdsWideband, mdsGlobalRegModule=mdsGlobalRegModule, PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsRoot=mdsRoot, mdsBroadband=mdsBroadband, mdsNarrowband=mdsNarrowband, mdsPointToPoint=mdsPointToPoint, mdsSoftware=mdsSoftware, mdsPointToMultiPoint=mdsPointToMultiPoint)
