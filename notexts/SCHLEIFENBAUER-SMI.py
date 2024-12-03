#
# PySNMP MIB module SCHLEIFENBAUER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/schleifenbauer/SCHLEIFENBAUER-SMI
# Produced by pysmi-1.1.12 at Tue Dec  3 12:40:39 2024
# On host fv-az658-333 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Gauge32, MibIdentifier, Counter64, ModuleIdentity, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, iso, TimeTicks, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibIdentifier", "Counter64", "ModuleIdentity", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "iso", "TimeTicks", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
schleifenbauer = ModuleIdentity((1, 3, 6, 1, 4, 1, 31034))
schleifenbauer.setRevisions(('2015-10-23 00:00',))
if mibBuilder.loadTexts: schleifenbauer.setLastUpdated('201510230000Z')
if mibBuilder.loadTexts: schleifenbauer.setOrganization('Schleifenbauer Engineering')
schleifenbauerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 11))
if mibBuilder.loadTexts: schleifenbauerProducts.setStatus('current')
schleifenbauerMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 12))
if mibBuilder.loadTexts: schleifenbauerMgmt.setStatus('current')
schleifenbauerModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 31034, 13))
if mibBuilder.loadTexts: schleifenbauerModules.setStatus('current')
mibBuilder.exportSymbols("SCHLEIFENBAUER-SMI", schleifenbauer=schleifenbauer, schleifenbauerModules=schleifenbauerModules, PYSNMP_MODULE_ID=schleifenbauer, schleifenbauerProducts=schleifenbauerProducts, schleifenbauerMgmt=schleifenbauerMgmt)
