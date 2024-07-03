#
# PySNMP MIB module SCHLEIFENBAUER-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-PRODUCTS-MIB
# Produced by pysmi-1.1.12 at Wed Jul  3 09:41:59 2024
# On host fv-az1766-730 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
schleifenbauerProducts, schleifenbauerModules = mibBuilder.importSymbols("SCHLEIFENBAUER-SMI", "schleifenbauerProducts", "schleifenbauerModules")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, Unsigned32, ModuleIdentity, Counter64, Gauge32, IpAddress, Integer32, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "Gauge32", "IpAddress", "Integer32", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
schleifenbauerProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034, 13, 2))
schleifenbauerProductsMIB.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauerProductsMIB.setOrganization('Schleifenbauer Engineering')
hpdu = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 1))
dpm3 = MibIdentifier((1, 3, 6, 1, 4, 1, 31034, 11, 2))
mibBuilder.exportSymbols("SCHLEIFENBAUER-PRODUCTS-MIB", PYSNMP_MODULE_ID=schleifenbauerProductsMIB, hpdu=hpdu, dpm3=dpm3, schleifenbauerProductsMIB=schleifenbauerProductsMIB)
