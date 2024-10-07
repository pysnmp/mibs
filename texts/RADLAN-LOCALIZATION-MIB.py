#
# PySNMP MIB module RADLAN-LOCALIZATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-LOCALIZATION-MIB
# Produced by pysmi-1.1.12 at Mon Oct  7 02:57:45 2024
# On host fv-az775-99 platform Linux version 6.8.0-1014-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, TimeTicks, Bits, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "TimeTicks", "Bits", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("RADLAN-LOCALIZATION-MIB", rlLocalizationLanguage=rlLocalizationLanguage, rlLocalizationMibVersion=rlLocalizationMibVersion, RlLanguage=RlLanguage, rlWEBlocalizationLanguage=rlWEBlocalizationLanguage, PYSNMP_MODULE_ID=rlLocalization, rlLocalization=rlLocalization, rlLocalizationFiles=rlLocalizationFiles)
