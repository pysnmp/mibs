#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-MIB
# Produced by pysmi-1.1.12 at Tue Dec  3 12:38:56 2024
# On host fv-az658-333 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, Counter64, enterprises, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, ModuleIdentity, NotificationType, MibIdentifier, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "enterprises", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "ModuleIdentity", "NotificationType", "MibIdentifier", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
if mibBuilder.loadTexts: nortel.setContactInfo('   7035 Ridge Road\n               Hanover, Maryland 21076\n               United States\n               Toll-free: +1-800-921-1144\n               Phone: +1-410-694-5700\n               Fax: +1-410-694-5750\n               www.ciena.com ')
if mibBuilder.loadTexts: nortel.setDescription('The Nortel Networks top-level MIB definition.')
nortelGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 29))
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-MIB", nortelGenericMIBs=nortelGenericMIBs, PYSNMP_MODULE_ID=nortel, opterametro=opterametro, nortel=nortel)
