#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.8 at Fri Jan  7 15:52:01 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, TimeTicks, ModuleIdentity, Counter32, Gauge32, MibIdentifier, IpAddress, Bits, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "ModuleIdentity", "Counter32", "Gauge32", "MibIdentifier", "IpAddress", "Bits", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
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
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAosIfPerfHistory=adGenAosIfPerfHistory, PYSNMP_MODULE_ID=adGenAOSCommonMib, adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSSnmp=adGenAOSSnmp, adGenAOSCommonMib=adGenAOSCommonMib, adGenAOSMux=adGenAOSMux, adGenAOSFan=adGenAOSFan, adGenAOSNetSync=adGenAOSNetSync, adGenAOSUnit=adGenAOSUnit, adGenAOSDyingGasp=adGenAOSDyingGasp, adAOSDownload=adAOSDownload, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSFileSystem=adGenAOSFileSystem)
