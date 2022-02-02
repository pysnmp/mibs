#
# PySNMP MIB module RADLAN-LOCALIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LOCALIZATION-MIB
# Produced by pysmi-1.1.8 at Wed Feb  2 19:34:59 2022
# On host fv-az33-564 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Bits, MibIdentifier, ModuleIdentity, IpAddress, TimeTicks, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Bits", "MibIdentifier", "ModuleIdentity", "IpAddress", "TimeTicks", "iso", "Counter32")
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
mibBuilder.exportSymbols("RADLAN-LOCALIZATION-MIB", rlLocalizationFiles=rlLocalizationFiles, rlLocalization=rlLocalization, rlLocalizationMibVersion=rlLocalizationMibVersion, PYSNMP_MODULE_ID=rlLocalization, rlWEBlocalizationLanguage=rlWEBlocalizationLanguage, RlLanguage=RlLanguage, rlLocalizationLanguage=rlLocalizationLanguage)
