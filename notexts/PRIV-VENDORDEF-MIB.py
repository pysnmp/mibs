#
# PySNMP MIB module PRIV-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Mon Nov 22 12:20:47 2021
# On host fv-az36-755 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, TimeTicks, IpAddress, Integer32, ModuleIdentity, MibIdentifier, iso, NotificationType, Unsigned32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "TimeTicks", "IpAddress", "Integer32", "ModuleIdentity", "MibIdentifier", "iso", "NotificationType", "Unsigned32", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
privateVendorOID = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
privateVendorOID.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: privateVendorOID.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: privateVendorOID.setOrganization('BATM Advanced Communication')
mibBuilder.exportSymbols("PRIV-VENDORDEF-MIB", privateVendorOID=privateVendorOID, PYSNMP_MODULE_ID=privateVendorOID)
