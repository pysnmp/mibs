#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.12 at Tue May 28 13:04:56 2024
# On host fv-az1789-536 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSCommon, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, MibIdentifier, Gauge32, ModuleIdentity, iso, ObjectIdentity, IpAddress, Unsigned32, NotificationType, Counter32, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "MibIdentifier", "Gauge32", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Unsigned32", "NotificationType", "Counter32", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSCommonMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 1))
adGenAOSCommonMib.setRevisions(('2015-01-05 00:00', '2014-11-05 22:05', '2014-09-10 00:00', '2013-08-23 00:00', '2007-08-23 00:00',))
if mibBuilder.loadTexts: adGenAOSCommonMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSCommonMib.setOrganization('ADTRAN, Inc.')
adGenAOSUnit = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 1))
adGenAOSSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2))
adAOSDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3))
adGenAOSCpuUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4))
adGenAOSMux = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 5))
adGenAOSFileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6))
adGenAosIfPerfHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 7))
adGenAOSFan = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 8))
adGenAOSNetSync = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 9))
adGenAOSOverTempProtection = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 10))
adGenAOSDyingGasp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 11))
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adAOSDownload=adAOSDownload, adGenAOSFan=adGenAOSFan, PYSNMP_MODULE_ID=adGenAOSCommonMib, adGenAOSCommonMib=adGenAOSCommonMib, adGenAOSDyingGasp=adGenAOSDyingGasp, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSMux=adGenAOSMux, adGenAOSNetSync=adGenAOSNetSync, adGenAOSSnmp=adGenAOSSnmp, adGenAOSUnit=adGenAOSUnit, adGenAOSCpuUtil=adGenAOSCpuUtil)
