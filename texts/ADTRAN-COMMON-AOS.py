#
# PySNMP MIB module ADTRAN-COMMON-AOS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-COMMON-AOS
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:08 2022
# On host fv-az77-149 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOS, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOS", "adGenAOSCommon")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Gauge32, ModuleIdentity, MibIdentifier, Counter32, Bits, TimeTicks, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Gauge32", "ModuleIdentity", "MibIdentifier", "Counter32", "Bits", "TimeTicks", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter64")
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
mibBuilder.exportSymbols("ADTRAN-COMMON-AOS", adGenAOSUnit=adGenAOSUnit, adGenAOSMux=adGenAOSMux, adGenAOSSnmp=adGenAOSSnmp, adGenAOSCommonMib=adGenAOSCommonMib, adGenAOSFileSystem=adGenAOSFileSystem, adGenAOSNetSync=adGenAOSNetSync, adAOSDownload=adAOSDownload, PYSNMP_MODULE_ID=adGenAOSCommonMib, adGenAosIfPerfHistory=adGenAosIfPerfHistory, adGenAOSOverTempProtection=adGenAOSOverTempProtection, adGenAOSDyingGasp=adGenAOSDyingGasp, adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSFan=adGenAOSFan)
