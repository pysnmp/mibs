#
# PySNMP MIB module WAYSTREAM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-SMI
# Produced by pysmi-1.1.12 at Tue Sep 17 12:28:50 2024
# On host fv-az1019-803 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.14 (main, Jul 16 2024, 19:03:10) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Integer32, Unsigned32, MibIdentifier, TimeTicks, Gauge32, Bits, iso, Counter32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Integer32", "Unsigned32", "MibIdentifier", "TimeTicks", "Gauge32", "Bits", "iso", "Counter32", "Counter64", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
waystream = ModuleIdentity((1, 3, 6, 1, 4, 1, 9303))
waystream.setRevisions(('2017-02-10 11:00', '2011-01-11 18:01', '2009-03-23 10:39', '2008-01-17 14:05', '2007-05-11 12:28',))
if mibBuilder.loadTexts: waystream.setLastUpdated('201702101100Z')
if mibBuilder.loadTexts: waystream.setOrganization('Waystream AB')
wsProduct = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 1))
if mibBuilder.loadTexts: wsProduct.setStatus('current')
wsConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2))
if mibBuilder.loadTexts: wsConfig.setStatus('current')
ipdConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 2, 1))
if mibBuilder.loadTexts: ipdConfig.setStatus('current')
wsExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 3))
if mibBuilder.loadTexts: wsExperiment.setStatus('current')
wsMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 4))
if mibBuilder.loadTexts: wsMgmt.setStatus('current')
wsModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 5))
if mibBuilder.loadTexts: wsModules.setStatus('current')
pfSW = ObjectIdentity((1, 3, 6, 1, 4, 1, 9303, 6))
if mibBuilder.loadTexts: pfSW.setStatus('current')
mibBuilder.exportSymbols("WAYSTREAM-SMI", wsModules=wsModules, wsConfig=wsConfig, PYSNMP_MODULE_ID=waystream, ipdConfig=ipdConfig, pfSW=pfSW, wsExperiment=wsExperiment, waystream=waystream, wsMgmt=wsMgmt, wsProduct=wsProduct)
