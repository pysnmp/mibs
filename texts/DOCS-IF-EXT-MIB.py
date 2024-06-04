#
# PySNMP MIB module DOCS-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DOCS-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 13:48:36 2024
# On host fv-az1110-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
docsIfCmtsCmStatusEntry, docsIfMib = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "docsIfMib")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ObjectIdentity, Counter32, iso, Unsigned32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, ModuleIdentity, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "ModuleIdentity", "NotificationType", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
docsIfExtMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 127, 21))
docsIfExtMib.setRevisions(('1900-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: docsIfExtMib.setRevisionsDescriptions(('Initial Version. ',))
if mibBuilder.loadTexts: docsIfExtMib.setLastUpdated('0011160000Z')
if mibBuilder.loadTexts: docsIfExtMib.setOrganization('IETF IPCDN Working Group')
if mibBuilder.loadTexts: docsIfExtMib.setContactInfo(' ')
if mibBuilder.loadTexts: docsIfExtMib.setDescription('This is the extension Module to rfc2670 DOCS-IF-MIB.')
class DocsisVersion(TextualConvention, Integer32):
    description = 'Indicates the docsis version number.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("docsis10", 1), ("docsis11", 2))

docsIfDocsisCapability = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisCapability.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisCapability.setDescription('Indication of the DOCSIS capability of the device.')
docsIfDocsisOperMode = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 2), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisOperMode.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisOperMode.setDescription('Indication whether the device has registered as a 1.0 or 1.1.\n            For CMTS and unregistered CM, it is always the same as \n            docsDocsisCapability.')
docsIfCmtsCmStatusExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 21, 3), )
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtTable.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtTable.setDescription('A set of objects in the CMTS, maintained for each\n            Cable Modem connected to this CMTS.')
docsIfCmtsCmStatusExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusExtEntry"))
docsIfCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtEntry.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtEntry.setDescription('Status information for a single Cable Modem.\n            An entry in this table exists for each Cable Modem\n            which is connected to the CMTS.')
docsIfCmtsCmStatusDocsisMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfCmtsCmStatusDocsisMode.setStatus('current')
if mibBuilder.loadTexts: docsIfCmtsCmStatusDocsisMode.setDescription('Indication whether the CM has registered as a 1.0 or 1.1 modem')
docsIfExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4))
docsIfExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1))
docsIfExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2))
docsIfExtCmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmCompliance = docsIfExtCmCompliance.setStatus('current')
if mibBuilder.loadTexts: docsIfExtCmCompliance.setDescription('The compliance statement.')
docsIfDocsisVersionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfDocsisVersionGroup = docsIfDocsisVersionGroup.setStatus('current')
if mibBuilder.loadTexts: docsIfDocsisVersionGroup.setDescription('Object group to indicates DOCSIS version.')
docsIfExtCmtsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfExtGroup"), ("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmtsCompliance = docsIfExtCmtsCompliance.setStatus('current')
if mibBuilder.loadTexts: docsIfExtCmtsCompliance.setDescription('The compliance statement.')
docsIfExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtGroup = docsIfExtGroup.setStatus('current')
if mibBuilder.loadTexts: docsIfExtGroup.setDescription('Mandatory implementation group for CMTS.')
mibBuilder.exportSymbols("DOCS-IF-EXT-MIB", docsIfCmtsCmStatusExtEntry=docsIfCmtsCmStatusExtEntry, docsIfCmtsCmStatusDocsisMode=docsIfCmtsCmStatusDocsisMode, docsIfExtGroup=docsIfExtGroup, docsIfExtCmCompliance=docsIfExtCmCompliance, docsIfExtGroups=docsIfExtGroups, DocsisVersion=DocsisVersion, docsIfCmtsCmStatusExtTable=docsIfCmtsCmStatusExtTable, docsIfDocsisCapability=docsIfDocsisCapability, docsIfDocsisVersionGroup=docsIfDocsisVersionGroup, PYSNMP_MODULE_ID=docsIfExtMib, docsIfExtCompliances=docsIfExtCompliances, docsIfExtMib=docsIfExtMib, docsIfExtCmtsCompliance=docsIfExtCmtsCompliance, docsIfExtConformance=docsIfExtConformance, docsIfDocsisOperMode=docsIfDocsisOperMode)
