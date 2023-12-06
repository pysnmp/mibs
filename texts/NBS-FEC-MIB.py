#
# PySNMP MIB module NBS-FEC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FEC-MIB
# Produced by pysmi-1.1.11 at Wed Dec  6 03:04:32 2023
# On host fv-az520-882 platform Linux version 6.2.0-1016-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter64, IpAddress, NotificationType, iso, Bits, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter64", "IpAddress", "NotificationType", "iso", "Bits", "TimeTicks", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsFecMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 232))
if mibBuilder.loadTexts: nbsFecMib.setLastUpdated('201504290000Z')
if mibBuilder.loadTexts: nbsFecMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsFecMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsFecMib.setDescription('Forward Error Correction')
class NbsFecCode(TextualConvention, Integer32):
    description = 'Particular FEC Algorithm/Code'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("notSupported", 0), ("noFec", 1), ("zero", 2), ("gfec", 3), ("ufec7", 4), ("ufec10", 5), ("ufec25", 6), ("hgfec7", 7), ("sdfec0", 8), ("sdfec1", 9), ("sdfec2", 10), ("sdfec3", 11), ("g975i4", 12), ("g975i7", 13), ("xfec7", 14), ("sdfec15", 15))

nbsFecCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 232, 1))
if mibBuilder.loadTexts: nbsFecCfgGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgGrp.setDescription('FEC configuration')
nbsFecCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 232, 1, 1), )
if mibBuilder.loadTexts: nbsFecCfgTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgTable.setDescription('FEC settings for all supported ports')
nbsFecCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1), ).setIndexNames((0, "NBS-FEC-MIB", "nbsFecCfgIfIndex"))
if mibBuilder.loadTexts: nbsFecCfgEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgEntry.setDescription('FEC settings for an individual port')
nbsFecCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgIfIndex.setDescription('The mib2 ifIndex')
nbsFecCfgCodeCaps = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeCaps.setDescription('This bitmask indicates which FEC codes this port can\n        support.\n\n        Bit 0 is reserved.\n\n        Subsequent bits refer to the NbsFecCode enumerated list.  Bit 1\n        corresponds to none(1), Bit 2 to zero(2) enumeration,\n        and so on.  A bit is set (1) if that code is appropriate\n        for this module, cleared (0) if unavailable.\n\n        OCTET STRING bitmasks count the leftmost bit (MSB) as 0.')
nbsFecCfgCodeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 3), NbsFecCode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeAdmin.setDescription('The administratively desired Forward Error Correction code')
nbsFecCfgCodeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 232, 1, 1, 1, 4), NbsFecCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setStatus('current')
if mibBuilder.loadTexts: nbsFecCfgCodeOper.setDescription('The operationally active Forward Error Correction code')
mibBuilder.exportSymbols("NBS-FEC-MIB", nbsFecCfgTable=nbsFecCfgTable, nbsFecMib=nbsFecMib, nbsFecCfgCodeOper=nbsFecCfgCodeOper, nbsFecCfgIfIndex=nbsFecCfgIfIndex, nbsFecCfgCodeAdmin=nbsFecCfgCodeAdmin, nbsFecCfgEntry=nbsFecCfgEntry, nbsFecCfgCodeCaps=nbsFecCfgCodeCaps, nbsFecCfgGrp=nbsFecCfgGrp, PYSNMP_MODULE_ID=nbsFecMib, NbsFecCode=NbsFecCode)
