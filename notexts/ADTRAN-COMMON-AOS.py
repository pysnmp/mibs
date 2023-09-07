#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.8 at Thu Sep  7 14:18:44 2023
# On host fv-az448-504 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
adGenAOS, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOS", "adGenAOSCommon")
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, ModuleIdentity, ObjectIdentity, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, IpAddress, iso, TimeTicks, Counter32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "IpAddress", "iso", "TimeTicks", "Counter32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAOSSnmp=adGenAOSSnmp, PYSNMP_MODULE_ID=adGenAOSCommonMib, adAOSDownload=adAOSDownload, adGenAOSFan=adGenAOSFan, adGenAOSUnit=adGenAOSUnit, adGenAOSCommonMib=adGenAOSCommonMib, adGenAOSNetSync=adGenAOSNetSync, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSDyingGasp=adGenAOSDyingGasp, adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSMux=adGenAOSMux)
