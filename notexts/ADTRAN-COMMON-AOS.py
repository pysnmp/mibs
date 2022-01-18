#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.8 at Tue Jan 18 13:37:28 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Bits, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, Integer32, IpAddress, NotificationType, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "Integer32", "IpAddress", "NotificationType", "TimeTicks", "ObjectIdentity")
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
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAOSDyingGasp=adGenAOSDyingGasp, adAOSDownload=adAOSDownload, adGenAOSFan=adGenAOSFan, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSUnit=adGenAOSUnit, adGenAOSSnmp=adGenAOSSnmp, PYSNMP_MODULE_ID=adGenAOSCommonMib, adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSNetSync=adGenAOSNetSync, adGenAOSCommonMib=adGenAOSCommonMib, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adGenAOSMux=adGenAOSMux)
