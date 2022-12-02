#
# PySNMP MIB module DOCS-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/DOCS-IF-EXT-MIB
# Produced by pysmi-1.1.8 at Fri Dec  2 17:01:45 2022
# On host fv-az563-842 platform Linux version 5.15.0-1023-azure by user runner
# Using Python version 3.10.8 (main, Oct 18 2022, 06:44:51) [GCC 11.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
docsIfCmtsCmStatusEntry, docsIfMib = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusEntry", "docsIfMib")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Integer32, Unsigned32, IpAddress, Gauge32, ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Integer32", "Unsigned32", "IpAddress", "Gauge32", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType")
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
mibBuilder.exportSymbols("DOCS-IF-EXT-MIB", docsIfExtCompliances=docsIfExtCompliances, docsIfCmtsCmStatusExtEntry=docsIfCmtsCmStatusExtEntry, docsIfCmtsCmStatusExtTable=docsIfCmtsCmStatusExtTable, docsIfExtCmCompliance=docsIfExtCmCompliance, docsIfCmtsCmStatusDocsisMode=docsIfCmtsCmStatusDocsisMode, docsIfDocsisCapability=docsIfDocsisCapability, docsIfExtMib=docsIfExtMib, DocsisVersion=DocsisVersion, docsIfDocsisOperMode=docsIfDocsisOperMode, docsIfExtConformance=docsIfExtConformance, PYSNMP_MODULE_ID=docsIfExtMib, docsIfExtGroups=docsIfExtGroups, docsIfExtCmtsCompliance=docsIfExtCmtsCompliance, docsIfDocsisVersionGroup=docsIfDocsisVersionGroup, docsIfExtGroup=docsIfExtGroup)
