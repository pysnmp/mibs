#
# PySNMP MIB module COLUBRIS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SMI.my
# Produced by pysmi-1.1.8 at Thu Sep 15 10:07:53 2022
# On host fv-az377-643 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Integer32, Unsigned32, Gauge32, TimeTicks, Bits, MibIdentifier, ModuleIdentity, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, iso, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "Unsigned32", "Gauge32", "TimeTicks", "Bits", "MibIdentifier", "ModuleIdentity", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "iso", "IpAddress")
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
mibBuilder.exportSymbols("COLUBRIS-SMI", colubrisExperiment=colubrisExperiment, colubrisMgmtV2=colubrisMgmtV2, colubrisMgmt=colubrisMgmt, extensions=extensions, PYSNMP_MODULE_ID=colubris, colubris=colubris, colubrisModules=colubrisModules, variation=variation, colubrisProducts=colubrisProducts)
