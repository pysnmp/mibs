#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 12:06:50 2024
# On host fv-az768-763 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, IpAddress, TimeTicks, Integer32, Unsigned32, MibIdentifier, NotificationType, ObjectIdentity, Counter64, iso, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "IpAddress", "TimeTicks", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "ObjectIdentity", "Counter64", "iso", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
if mibBuilder.loadTexts: nortel.setContactInfo('   7035 Ridge Road\n               Hanover, Maryland 21076\n               United States\n               Toll-free: +1-800-921-1144\n               Phone: +1-410-694-5700\n               Fax: +1-410-694-5750\n               www.ciena.com ')
if mibBuilder.loadTexts: nortel.setDescription('The Nortel Networks top-level MIB definition.')
nortelGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 29))
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-MIB", nortelGenericMIBs=nortelGenericMIBs, opterametro=opterametro, nortel=nortel, PYSNMP_MODULE_ID=nortel)
