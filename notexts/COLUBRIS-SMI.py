#
# PySNMP MIB module COLUBRIS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-SMI.my
# Produced by pysmi-1.1.3 at Wed Dec  8 21:19:16 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ModuleIdentity, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ObjectIdentity, Counter64, MibIdentifier, Bits, TimeTicks, IpAddress, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ModuleIdentity", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "Gauge32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("COLUBRIS-SMI", colubrisModules=colubrisModules, colubris=colubris, PYSNMP_MODULE_ID=colubris, colubrisExperiment=colubrisExperiment, variation=variation, extensions=extensions, colubrisProducts=colubrisProducts, colubrisMgmtV2=colubrisMgmtV2, colubrisMgmt=colubrisMgmt)
