#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.3 at Wed Dec  8 18:57:10 2021
# On host fv-az121-73 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, Bits, TimeTicks, enterprises, Counter64, Gauge32, Unsigned32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Bits", "TimeTicks", "enterprises", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arbornetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694))
arbornetworks.setRevisions(('2013-11-14 00:00', '2013-08-19 00:00', '2011-07-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2005-09-12 00:00',))
if mibBuilder.loadTexts: arbornetworks.setLastUpdated('201311140000Z')
if mibBuilder.loadTexts: arbornetworks.setOrganization('Arbor Networks, Inc.')
arbornetworksProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 1))
if mibBuilder.loadTexts: arbornetworksProducts.setStatus('current')
arborExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 2))
if mibBuilder.loadTexts: arborExperimental.setStatus('current')
mibBuilder.exportSymbols("ARBOR-SMI", PYSNMP_MODULE_ID=arbornetworks, arborExperimental=arborExperimental, arbornetworksProducts=arbornetworksProducts, arbornetworks=arbornetworks)
