#
# PySNMP MIB module BEGEMOT-HOSTRES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HOSTRES-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 12:21:54 2024
# On host fv-az1385-751 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, iso, Unsigned32, Gauge32, ObjectIdentity, Counter32, Counter64, MibIdentifier, IpAddress, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "iso", "Unsigned32", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BEGEMOT-HOSTRES-MIB", begemotHostresObjects=begemotHostresObjects, begemotHrSWRunUpdate=begemotHrSWRunUpdate, begemotHrSWInstalledUpdate=begemotHrSWInstalledUpdate, begemotHrStorageUpdate=begemotHrStorageUpdate, begemotHostres=begemotHostres, PYSNMP_MODULE_ID=begemotHostres, begemotHrNetworkUpdate=begemotHrNetworkUpdate, begemotHrDiskStorageUpdate=begemotHrDiskStorageUpdate, begemotHrFSUpdate=begemotHrFSUpdate, begemotHrPkgDir=begemotHrPkgDir)
