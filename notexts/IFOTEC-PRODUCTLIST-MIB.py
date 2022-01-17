#
# PySNMP MIB module IFOTEC-PRODUCTLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ifotec/IFOTEC-PRODUCTLIST-MIB
# Produced by pysmi-1.1.8 at Mon Jan 17 18:49:43 2022
# On host fv-az33-58 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ifotec, = mibBuilder.importSymbols("IFOTEC-SMI", "ifotec")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, ObjectIdentity, iso, TimeTicks, Bits, Counter32, IpAddress, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ObjectIdentity", "iso", "TimeTicks", "Bits", "Counter32", "IpAddress", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ifotecProductList = ModuleIdentity((1, 3, 6, 1, 4, 1, 21362, 100))
if mibBuilder.loadTexts: ifotecProductList.setLastUpdated('202007290000Z')
if mibBuilder.loadTexts: ifotecProductList.setOrganization('IFOTEC')
ifotecEthernetProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1))
ifotecL2ManagedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4))
ifotecINETFamilly = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3))
INET_2GE2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 1)).setLabel("INET-2GE2GF-AS-101")
INET_2GP2GF_AS_101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 2)).setLabel("INET-2GP2GF-AS-101")
INET_4GE2GF_KS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 3)).setLabel("INET-4GE2GF-KS-001")
INET_4GP2GF_AS_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 4)).setLabel("INET-4GP2GF-AS-001")
INET_4GE2GF2XF_R1_001 = MibIdentifier((1, 3, 6, 1, 4, 1, 21362, 100, 1, 4, 3, 5)).setLabel("INET-4GE2GF2XF-R1-001")
mibBuilder.exportSymbols("IFOTEC-PRODUCTLIST-MIB", ifotecL2ManagedSwitches=ifotecL2ManagedSwitches, INET_4GE2GF2XF_R1_001=INET_4GE2GF2XF_R1_001, INET_2GP2GF_AS_101=INET_2GP2GF_AS_101, ifotecINETFamilly=ifotecINETFamilly, ifotecEthernetProducts=ifotecEthernetProducts, INET_2GE2GF_AS_101=INET_2GE2GF_AS_101, INET_4GE2GF_KS_001=INET_4GE2GF_KS_001, ifotecProductList=ifotecProductList, PYSNMP_MODULE_ID=ifotecProductList, INET_4GP2GF_AS_001=INET_4GP2GF_AS_001)
