#
# PySNMP MIB module BEGEMOT-HOSTRES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HOSTRES-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 12:00:24 2024
# On host fv-az1530-743 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, TimeTicks, Counter32, Integer32, Gauge32, NotificationType, ObjectIdentity, Unsigned32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "Integer32", "Gauge32", "NotificationType", "ObjectIdentity", "Unsigned32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotHostres = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 202))
if mibBuilder.loadTexts: begemotHostres.setLastUpdated('200601030000Z')
if mibBuilder.loadTexts: begemotHostres.setOrganization('German Aerospace Center')
begemotHostresObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1))
begemotHrStorageUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 1), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrStorageUpdate.setStatus('current')
begemotHrFSUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 2), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrFSUpdate.setStatus('current')
begemotHrDiskStorageUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 3), TimeTicks().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrDiskStorageUpdate.setStatus('current')
begemotHrNetworkUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 4), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrNetworkUpdate.setStatus('current')
begemotHrSWInstalledUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 5), TimeTicks().clone(1200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrSWInstalledUpdate.setStatus('current')
begemotHrSWRunUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 6), TimeTicks().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrSWRunUpdate.setStatus('current')
begemotHrPkgDir = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 7), OctetString().clone('/var/db/pkg')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrPkgDir.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-HOSTRES-MIB", begemotHrSWInstalledUpdate=begemotHrSWInstalledUpdate, PYSNMP_MODULE_ID=begemotHostres, begemotHostresObjects=begemotHostresObjects, begemotHrDiskStorageUpdate=begemotHrDiskStorageUpdate, begemotHrSWRunUpdate=begemotHrSWRunUpdate, begemotHostres=begemotHostres, begemotHrNetworkUpdate=begemotHrNetworkUpdate, begemotHrPkgDir=begemotHrPkgDir, begemotHrFSUpdate=begemotHrFSUpdate, begemotHrStorageUpdate=begemotHrStorageUpdate)
