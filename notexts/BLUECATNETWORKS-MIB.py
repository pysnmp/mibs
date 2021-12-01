#
# PySNMP MIB module BLUECATNETWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BLUECATNETWORKS-MIB
# Produced by pysmi-1.1.3 at Wed Dec  1 17:38:06 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, Counter64, ObjectIdentity, enterprises, iso, TimeTicks, MibIdentifier, Counter32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "Counter64", "ObjectIdentity", "enterprises", "iso", "TimeTicks", "MibIdentifier", "Counter32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecatnetworksId = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 1))
bluecatnetworksId.setRevisions(('2010-11-30 00:00',))
if mibBuilder.loadTexts: bluecatnetworksId.setLastUpdated('201011300000Z')
if mibBuilder.loadTexts: bluecatnetworksId.setOrganization('BlueCat Networks Inc.')
bluecatnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 13315))
appliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 100))
mibBuilder.exportSymbols("BLUECATNETWORKS-MIB", bluecatnetworksId=bluecatnetworksId, PYSNMP_MODULE_ID=bluecatnetworksId, appliances=appliances, bluecatnetworks=bluecatnetworks)
