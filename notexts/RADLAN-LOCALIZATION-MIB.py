#
# PySNMP MIB module RADLAN-LOCALIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LOCALIZATION-MIB
# Produced by pysmi-1.1.8 at Tue Feb  8 23:21:51 2022
# On host fv-az42-507 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Integer32, Counter64, NotificationType, Unsigned32, ModuleIdentity, Gauge32, IpAddress, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "Counter64", "NotificationType", "Unsigned32", "ModuleIdentity", "Gauge32", "IpAddress", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
rlLocalization = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 103))
rlLocalization.setRevisions(('2005-03-15 00:00',))
if mibBuilder.loadTexts: rlLocalization.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: rlLocalization.setOrganization('Radlan Computer Communications Ltd.')
class RlLanguage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("original", 1), ("translated", 2))

rlLocalizationMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationMibVersion.setStatus('current')
rlLocalizationLanguage = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 5), RlLanguage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLocalizationLanguage.setStatus('current')
rlWEBlocalizationLanguage = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 6), RlLanguage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWEBlocalizationLanguage.setStatus('current')
rlLocalizationFiles = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-translated-files", 1), ("two-messages-files", 2), ("two-web-files", 3), ("two-messages-and-web-files", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationFiles.setStatus('current')
mibBuilder.exportSymbols("RADLAN-LOCALIZATION-MIB", RlLanguage=RlLanguage, PYSNMP_MODULE_ID=rlLocalization, rlLocalizationLanguage=rlLocalizationLanguage, rlWEBlocalizationLanguage=rlWEBlocalizationLanguage, rlLocalization=rlLocalization, rlLocalizationFiles=rlLocalizationFiles, rlLocalizationMibVersion=rlLocalizationMibVersion)
