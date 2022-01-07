#
# PySNMP MIB module ADTRAN-AOS-MEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-MEF-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 00:05:55 2022
# On host fv-az77-763 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSMef, adGenAOS = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSMef", "adGenAOS")
adIdentityShared, adShared = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared", "adShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, NotificationType, Integer32, Unsigned32, ObjectIdentity, Gauge32, Counter64, Bits, IpAddress, ModuleIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "Gauge32", "Counter64", "Bits", "IpAddress", "ModuleIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenAOSMefMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 9))
adGenAOSMefMib.setRevisions(('2014-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSMefMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSMefMib.setLastUpdated('201409100000Z')
if mibBuilder.loadTexts: adGenAOSMefMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSMefMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                901 Explorer Blvd.\n                Huntsville, AL 35806\n\n                Tel: +1 800 726-8663\n                Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSMefMib.setDescription('This MIB defines the Adtran OS Common enterprise tree node.  It\n                         provides a basis for the definition of all other Adtran OS MEF\n                         MIBs.')
adGenAosMefPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 1))
adGenAosMefPerCosPerUniPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 2))
adGenAosMefPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 3))
adGenAosMefPerCosPerEvcPerfHistoryMib = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 9, 4))
mibBuilder.exportSymbols("ADTRAN-AOS-MEF-MIB", adGenAosMefPerEvcPerfHistoryMib=adGenAosMefPerEvcPerfHistoryMib, adGenAosMefPerUniPerfHistoryMib=adGenAosMefPerUniPerfHistoryMib, adGenAOSMefMib=adGenAOSMefMib, adGenAosMefPerCosPerUniPerfHistoryMib=adGenAosMefPerCosPerUniPerfHistoryMib, PYSNMP_MODULE_ID=adGenAOSMefMib, adGenAosMefPerCosPerEvcPerfHistoryMib=adGenAosMefPerCosPerEvcPerfHistoryMib)
