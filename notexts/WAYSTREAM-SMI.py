#
# PySNMP MIB module WAYSTREAM-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/waystream/WAYSTREAM-SMI
# Produced by pysmi-1.1.8 at Wed Feb  2 18:31:41 2022
# On host fv-az83-345 platform Linux version 5.11.0-1027-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, ModuleIdentity, Bits, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, enterprises, TimeTicks, Gauge32, Integer32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "Bits", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "enterprises", "TimeTicks", "Gauge32", "Integer32", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("WAYSTREAM-SMI", wsProduct=wsProduct, ipdConfig=ipdConfig, pfSW=pfSW, waystream=waystream, wsExperiment=wsExperiment, PYSNMP_MODULE_ID=waystream, wsConfig=wsConfig, wsModules=wsModules, wsMgmt=wsMgmt)
