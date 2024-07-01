#
# PySNMP MIB module DOCS-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DOCS-IF-EXT-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 09:16:33 2024
# On host fv-az735-465 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
docsIfMib, docsIfCmtsCmStatusEntry = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfMib", "docsIfCmtsCmStatusEntry")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, ObjectIdentity, Counter64, Gauge32, Bits, TimeTicks, iso, Integer32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "Bits", "TimeTicks", "iso", "Integer32", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
docsIfExtMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 127, 21))
docsIfExtMib.setRevisions(('1900-10-08 00:00',))
if mibBuilder.loadTexts: docsIfExtMib.setLastUpdated('0011160000Z')
if mibBuilder.loadTexts: docsIfExtMib.setOrganization('IETF IPCDN Working Group')
class DocsisVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("docsis10", 1), ("docsis11", 2))

docsIfDocsisCapability = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisCapability.setStatus('current')
docsIfDocsisOperMode = MibScalar((1, 3, 6, 1, 2, 1, 10, 127, 21, 2), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfDocsisOperMode.setStatus('current')
docsIfCmtsCmStatusExtTable = MibTable((1, 3, 6, 1, 2, 1, 10, 127, 21, 3), )
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtTable.setStatus('current')
docsIfCmtsCmStatusExtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1), )
docsIfCmtsCmStatusEntry.registerAugmentions(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusExtEntry"))
docsIfCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
if mibBuilder.loadTexts: docsIfCmtsCmStatusExtEntry.setStatus('current')
docsIfCmtsCmStatusDocsisMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1, 1), DocsisVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsIfCmtsCmStatusDocsisMode.setStatus('current')
docsIfExtConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4))
docsIfExtCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1))
docsIfExtGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2))
docsIfExtCmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmCompliance = docsIfExtCmCompliance.setStatus('current')
docsIfDocsisVersionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 1)).setObjects(("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"), ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfDocsisVersionGroup = docsIfDocsisVersionGroup.setStatus('current')
docsIfExtCmtsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfExtGroup"), ("DOCS-IF-EXT-MIB", "docsIfDocsisVersionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtCmtsCompliance = docsIfExtCmtsCompliance.setStatus('current')
docsIfExtGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 2)).setObjects(("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsIfExtGroup = docsIfExtGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-IF-EXT-MIB", docsIfExtCmCompliance=docsIfExtCmCompliance, docsIfCmtsCmStatusExtEntry=docsIfCmtsCmStatusExtEntry, docsIfCmtsCmStatusExtTable=docsIfCmtsCmStatusExtTable, docsIfCmtsCmStatusDocsisMode=docsIfCmtsCmStatusDocsisMode, docsIfExtCmtsCompliance=docsIfExtCmtsCompliance, docsIfExtCompliances=docsIfExtCompliances, PYSNMP_MODULE_ID=docsIfExtMib, docsIfDocsisOperMode=docsIfDocsisOperMode, DocsisVersion=DocsisVersion, docsIfExtGroup=docsIfExtGroup, docsIfExtConformance=docsIfExtConformance, docsIfExtGroups=docsIfExtGroups, docsIfExtMib=docsIfExtMib, docsIfDocsisVersionGroup=docsIfDocsisVersionGroup, docsIfDocsisCapability=docsIfDocsisCapability)
