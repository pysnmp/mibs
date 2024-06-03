#
# PySNMP MIB module RADLAN-LOCALIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LOCALIZATION-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 14:07:18 2024
# On host fv-az914-826 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, MibIdentifier, Gauge32, Counter32, Bits, Unsigned32, ModuleIdentity, IpAddress, TimeTicks, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "Bits", "Unsigned32", "ModuleIdentity", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
rlLocalization = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 103))
rlLocalization.setRevisions(('2005-03-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlLocalization.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlLocalization.setLastUpdated('200503150000Z')
if mibBuilder.loadTexts: rlLocalization.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlLocalization.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlLocalization.setDescription('The private MIB module definition for product localization.')
class RlLanguage(TextualConvention, Integer32):
    description = 'The language enumeration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("original", 1), ("translated", 2))

rlLocalizationMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlLocalizationMibVersion.setDescription("MIB's version, the current version is 1.")
rlLocalizationLanguage = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 5), RlLanguage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLocalizationLanguage.setStatus('current')
if mibBuilder.loadTexts: rlLocalizationLanguage.setDescription('The language for diagnostic messages, CLI messages and CLI help.')
rlWEBlocalizationLanguage = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 6), RlLanguage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWEBlocalizationLanguage.setStatus('current')
if mibBuilder.loadTexts: rlWEBlocalizationLanguage.setDescription('The language for WEB GUI.')
rlLocalizationFiles = MibScalar((1, 3, 6, 1, 4, 1, 89, 103, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("no-translated-files", 1), ("two-messages-files", 2), ("two-web-files", 3), ("two-messages-and-web-files", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLocalizationFiles.setStatus('current')
if mibBuilder.loadTexts: rlLocalizationFiles.setDescription('The language for WEB GUI.')
mibBuilder.exportSymbols("RADLAN-LOCALIZATION-MIB", rlLocalizationLanguage=rlLocalizationLanguage, rlLocalizationMibVersion=rlLocalizationMibVersion, rlWEBlocalizationLanguage=rlWEBlocalizationLanguage, rlLocalization=rlLocalization, RlLanguage=RlLanguage, PYSNMP_MODULE_ID=rlLocalization, rlLocalizationFiles=rlLocalizationFiles)
