#
# PySNMP MIB module NBS-FEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FEC-MIB
# Produced by pysmi-1.1.3 at Wed Dec  8 18:19:32 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, TimeTicks, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, MibIdentifier, Gauge32, iso, Bits, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "TimeTicks", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "MibIdentifier", "Gauge32", "iso", "Bits", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nbsFecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 232))
if mibBuilder.loadTexts: nbsFecMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsFecMib.setOrganization('NBS')
class NbsFecCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("notSupported", 0), ("noFec", 1), ("zero", 2), ("gfec", 3), ("ufec7", 4), ("ufec10", 5), ("ufec25", 6), ("hgfec7", 7), ("sdfec0", 8), ("sdfec1", 9), ("sdfec2", 10), ("sdfec3", 11), ("g975i4", 12), ("g975i7", 13), ("xfec7", 14), ("sdfec15", 15))

nbsFecCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 232, 1))
if mibBuilder.loadTexts: nbsFecCfgGrp.setStatus('current')
nbsFecCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 232, 1, 1), )
if mibBuilder.loadTexts: nbsFecCfgTable.setStatus('current')
nbsFecCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1), ).setIndexNames((0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"))
if mibBuilder.loadTexts: nbsFecCfgEntry.setStatus('current')
nbsFecCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setStatus('current')
nbsFecCfgCodeCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setStatus('current')
nbsFecCfgCodeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3), NbsFecCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setStatus('current')
nbsFecCfgCodeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4), NbsFecCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setStatus('current')
mibBuilder.exportSymbols("NBS-FEC-MIB", nbsFecCfgGrp=nbsFecCfgGrp, nbsFecCfgEntry=nbsFecCfgEntry, nbsFecCfgIfIndex=nbsFecCfgIfIndex, nbsFecCfgCodeAdmin=nbsFecCfgCodeAdmin, PYSNMP_MODULE_ID=nbsFecMib, nbsFecCfgCodeOper=nbsFecCfgCodeOper, NbsFecCode=NbsFecCode, nbsFecMib=nbsFecMib, nbsFecCfgCodeCaps=nbsFecCfgCodeCaps, nbsFecCfgTable=nbsFecCfgTable)
