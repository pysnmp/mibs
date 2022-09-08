#
# PySNMP MIB module COLUBRIS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SMI.my
# Produced by pysmi-1.1.8 at Thu Sep  8 09:53:47 2022
# On host fv-az173-382 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, MibIdentifier, ObjectIdentity, Gauge32, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, enterprises, TimeTicks, Integer32, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "MibIdentifier", "ObjectIdentity", "Gauge32", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "enterprises", "TimeTicks", "Integer32", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubris = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744))
if mibBuilder.loadTexts: colubris.setLastUpdated('200402100000Z')
if mibBuilder.loadTexts: colubris.setOrganization('Colubris Networks, Inc.')
colubrisProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 1))
if mibBuilder.loadTexts: colubrisProducts.setStatus('current')
colubrisMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 2))
if mibBuilder.loadTexts: colubrisMgmt.setStatus('deprecated')
colubrisExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 3))
if mibBuilder.loadTexts: colubrisExperiment.setStatus('current')
colubrisModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 4))
if mibBuilder.loadTexts: colubrisModules.setStatus('current')
colubrisMgmtV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 5))
if mibBuilder.loadTexts: colubrisMgmtV2.setStatus('current')
extensions = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 6))
if mibBuilder.loadTexts: extensions.setStatus('current')
variation = ObjectIdentity((1, 3, 6, 1, 4, 1, 8744, 7))
if mibBuilder.loadTexts: variation.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-SMI", colubrisMgmtV2=colubrisMgmtV2, colubrisExperiment=colubrisExperiment, colubrisProducts=colubrisProducts, colubris=colubris, PYSNMP_MODULE_ID=colubris, extensions=extensions, variation=variation, colubrisMgmt=colubrisMgmt, colubrisModules=colubrisModules)
