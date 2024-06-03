#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/NORTEL-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 11:24:56 2024
# On host fv-az1766-862 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, NotificationType, Unsigned32, IpAddress, Counter64, Integer32, ModuleIdentity, ObjectIdentity, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Integer32", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
if mibBuilder.loadTexts: nortel.setContactInfo('   7035 Ridge Road\n               Hanover, Maryland 21076\n               United States\n               Toll-free: +1-800-921-1144\n               Phone: +1-410-694-5700\n               Fax: +1-410-694-5750\n               www.ciena.com ')
if mibBuilder.loadTexts: nortel.setDescription('The Nortel Networks top-level MIB definition.')
nortelGenericMIBs = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 29))
opterametro = MibIdentifier((1, 3, 6, 1, 4, 1, 562, 68))
mibBuilder.exportSymbols("NORTEL-MIB", opterametro=opterametro, PYSNMP_MODULE_ID=nortel, nortelGenericMIBs=nortelGenericMIBs, nortel=nortel)
