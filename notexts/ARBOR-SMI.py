#
# PySNMP MIB module ARBOR-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-SMI
# Produced by pysmi-1.1.0 at Fri Nov 19 14:50:48 2021
# On host fv-az33-360 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, iso, Gauge32, TimeTicks, Bits, ModuleIdentity, Unsigned32, enterprises, NotificationType, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "iso", "Gauge32", "TimeTicks", "Bits", "ModuleIdentity", "Unsigned32", "enterprises", "NotificationType", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
arbornetworks = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694))
arbornetworks.setRevisions(('2013-11-14 00:00', '2013-08-19 00:00', '2011-07-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2005-09-12 00:00',))
if mibBuilder.loadTexts: arbornetworks.setLastUpdated('201311140000Z')
if mibBuilder.loadTexts: arbornetworks.setOrganization('Arbor Networks, Inc.')
arbornetworksProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 1))
if mibBuilder.loadTexts: arbornetworksProducts.setStatus('current')
arborExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 9694, 2))
if mibBuilder.loadTexts: arborExperimental.setStatus('current')
mibBuilder.exportSymbols("ARBOR-SMI", arborExperimental=arborExperimental, arbornetworks=arbornetworks, arbornetworksProducts=arbornetworksProducts, PYSNMP_MODULE_ID=arbornetworks)
