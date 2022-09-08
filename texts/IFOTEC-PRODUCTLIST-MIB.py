#
# PySNMP MIB module IFOTEC-PRODUCTLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ifotec/IFOTEC-PRODUCTLIST-MIB
# Produced by pysmi-1.1.8 at Thu Sep  8 09:55:36 2022
# On host fv-az173-382 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifotec, = mibBuilder.importSymbols("IFOTEC-SMI", "ifotec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, iso, TimeTicks, MibIdentifier, Integer32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ObjectIdentity, IpAddress, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ifotecProductList = ModuleIdentity((1, 3, 6, 1, 4, 1, 21362, 100))
if mibBuilder.loadTexts: ifotecProductList.setLastUpdated('202007290000Z')
if mibBuilder.loadTexts: ifotecProductList.setOrganization('IFOTEC')
if mibBuilder.loadTexts: ifotecProductList.setContactInfo('contact@ifotec.com')
if mibBuilder.loadTexts: ifotecProductList.setDescription('Product list of IFOTEC enterprise.')
ifotecEthernetProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1))
ifotecL2ManagedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4))
ifotecINETFamilly = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3))
INET_2GE2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 1)).setLabel("INET-2GE2GF-AS-101")
INET_2GP2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 2)).setLabel("INET-2GP2GF-AS-101")
INET_4GE2GF_KS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 3)).setLabel("INET-4GE2GF-KS-001")
INET_4GP2GF_AS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 4)).setLabel("INET-4GP2GF-AS-001")
INET_4GE2GF2XF_R1_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 5)).setLabel("INET-4GE2GF2XF-R1-001")
mibBuilder.exportSymbols("IFOTEC-PRODUCTLIST-MIB", ifotecEthernetProducts=ifotecEthernetProducts, ifotecL2ManagedSwitches=ifotecL2ManagedSwitches, INET_4GE2GF2XF_R1_001=INET_4GE2GF2XF_R1_001, PYSNMP_MODULE_ID=ifotecProductList, INET_2GP2GF_AS_101=INET_2GP2GF_AS_101, INET_4GE2GF_KS_001=INET_4GE2GF_KS_001, ifotecProductList=ifotecProductList, INET_2GE2GF_AS_101=INET_2GE2GF_AS_101, INET_4GP2GF_AS_001=INET_4GP2GF_AS_001, ifotecINETFamilly=ifotecINETFamilly)
