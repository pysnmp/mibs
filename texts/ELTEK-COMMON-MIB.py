#
# PySNMP MIB module ELTEK-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltek/ELTEK-COMMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan  2 13:11:41 2023
# On host fv-az574-39 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, MibIdentifier, ModuleIdentity, Counter32, mib_2, enterprises, ObjectIdentity, Unsigned32, IpAddress, Integer32, Bits, iso, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "MibIdentifier", "ModuleIdentity", "Counter32", "mib-2", "enterprises", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "Bits", "iso", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltek = ModuleIdentity((1, 3, 6, 1, 4, 1, 12148))
eltek.setRevisions(('2015-01-03 08:25', '2010-10-29 08:29', '2009-03-12 15:15', '2008-01-30 11:49', '2007-06-22 11:27', '2005-09-07 12:38', '2005-06-28 11:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: eltek.setRevisionsDescriptions(('Updates in miscellaneous info fields.', "Added traps and OID's for SolarChargers.\n\t\tAdded reading of values on programmable inputs of IO Monitor.", 'Added support for external IO monitor and Load monitor units.\n\t\tChanges are done in the MIB to accomodate the v2c standard.', 'Some OIDs were added to this revision. Since all new stuff are additions and no existing information was moved, this V3 revision stays in branch 9. enjoy!', 'Branch 9, contains mainly changes in the Traps format. The traps now meets SNMP v2c specification.', 'added battery test and boost start/stop and ac voltages', 'First revision',))
if mibBuilder.loadTexts: eltek.setLastUpdated('201501030825Z')
if mibBuilder.loadTexts: eltek.setOrganization('ELTEK dcSystem MIB Working Group')
if mibBuilder.loadTexts: eltek.setContactInfo('Eltek R&D.\n\t\t      Postal: Eltek AS\n\t\t      P.O. Box 3043\n\t\t      N-3003 Drammen\n\t\t      Norway\n\t\t      Tel: +47-32 20 32 00\n\t\t      Fax: +47-32 20 31 20\n\t\t      web:  www.eltek.com')
if mibBuilder.loadTexts: eltek.setDescription('An ongoing effort toward a generic MIB for all ELTEK products.\n\t\tBranch overview:\n\t\tAeongold branch will be 1\n\t\tAL175 branch will be 2\n\t\tAL6000 branch will be 3\n\t\tInternal used branch will be 4\n\t\tInternal used branch will be 5\n\t\tOEM Smartpack branch will be 6\n\t\tELTEK Common branch will be 7 (SmartPack, MCU, AEON w/WebPower sw V2.x)\n\t\tELTEK Distributed branch will be 8 (SmartPack w/WebPower sw V3.x)\n\t\tELTEK Distributed V2 branch will be 9 (SmartPack w/WebPower sw V4.0)\n\t\tELTEK Distributed V3 branch will be 9 (SmartPack w/WebPower sw V4.1)\n\t\tELTEK Distributed V4 branch will be 9 (SmartPack w/WebPower sw V4.1, V4.2, V4.3 and compack 1.xx)\n\t\tELTEK Distributed V5 branch will be 9 (SmartPack w/WebPower sw V4.6)\n\t\tELTEK Distributed V6 branch will be 9 (SmartPack w/WebPower sw V4.6, Smartpack2 V1.1)\n\t\tELTEK Distributed V7 branch will be 9 (SmartPack w/WebPower sw V4.7, V4.8, ComPack V1.04, Smartpack2 V1.1, V1.2)\n\t\tELTEK Distributed V8 branch will be 9 (SmartPack w/WebPower sw V4.9, ComPack V1.04, Smartpack2 V1.1, V1.2)')
mibBuilder.exportSymbols("ELTEK-COMMON-MIB", PYSNMP_MODULE_ID=eltek, eltek=eltek)
