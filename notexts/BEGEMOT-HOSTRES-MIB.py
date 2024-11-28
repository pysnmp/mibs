#
# PySNMP MIB module BEGEMOT-HOSTRES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HOSTRES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 28 03:01:57 2024
# On host fv-az885-149 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ModuleIdentity, Counter32, Gauge32, Bits, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "Counter64", "Integer32")
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
mibBuilder.exportSymbols("BEGEMOT-HOSTRES-MIB", begemotHrSWInstalledUpdate=begemotHrSWInstalledUpdate, begemotHrNetworkUpdate=begemotHrNetworkUpdate, begemotHostresObjects=begemotHostresObjects, PYSNMP_MODULE_ID=begemotHostres, begemotHrPkgDir=begemotHrPkgDir, begemotHrStorageUpdate=begemotHrStorageUpdate, begemotHostres=begemotHostres, begemotHrFSUpdate=begemotHrFSUpdate, begemotHrSWRunUpdate=begemotHrSWRunUpdate, begemotHrDiskStorageUpdate=begemotHrDiskStorageUpdate)
