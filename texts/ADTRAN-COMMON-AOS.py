#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.12 at Tue May 28 12:30:49 2024
# On host fv-az768-311 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
adGenAOSCommon, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Gauge32, Bits, Counter64, Unsigned32, IpAddress, TimeTicks, ObjectIdentity, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "Counter64", "Unsigned32", "IpAddress", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSCommonMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 1))
adGenAOSCommonMib.setRevisions(('2015-01-05 00:00', '2014-11-05 22:05', '2014-09-10 00:00', '2013-08-23 00:00', '2007-08-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSCommonMib.setRevisionsDescriptions(('Added adGenAOSDyingGasp.', 'Added adGenAOSOverTempProtection.', 'Fixed compile error and cleaned up warnings.', 'Added adGenAosIfPerfHistory.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSCommonMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSCommonMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSCommonMib.setContactInfo('Technical Support Dept.\n            Postal: ADTRAN, Inc.\n            901 Explorer Blvd.\n            Huntsville, AL 35806\n\n            Tel: +1 800 726-8663\n            Fax: +1 256 963 6217\n            E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSCommonMib.setDescription('This MIB defines the Adtran OS Common enterprise tree node.  It\n\t\t     provides a basis for the definition of all other Adtran OS Common\n\t\t     MIBs.')
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
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSSnmp=adGenAOSSnmp, adGenAOSUnit=adGenAOSUnit, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSNetSync=adGenAOSNetSync, PYSNMP_MODULE_ID=adGenAOSCommonMib, adGenAOSCommonMib=adGenAOSCommonMib, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adGenAOSDyingGasp=adGenAOSDyingGasp, adAOSDownload=adAOSDownload, adGenAOSMux=adGenAOSMux, adGenAOSFan=adGenAOSFan)
