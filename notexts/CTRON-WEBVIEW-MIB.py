#
# PySNMP MIB module CTRON-WEBVIEW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-WEBVIEW-MIB
# Produced by pysmi-1.1.12 at Mon Jun  3 13:11:45 2024
# On host fv-az915-96 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ctApplication, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctApplication")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, Unsigned32, NotificationType, MibIdentifier, IpAddress, Gauge32, TimeTicks, Counter32, iso, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Unsigned32", "NotificationType", "MibIdentifier", "IpAddress", "Gauge32", "TimeTicks", "Counter32", "iso", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctWebView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4))
ctEwvConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1))
ctEwvStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 2))
ctEwvDocSupport = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1))
ctEwvDocSupportAdmin = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdmin.setStatus('mandatory')
ctEwvDocSupportLocation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportLocation.setStatus('mandatory')
ctEwvDocSupportAdminUID = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportAdminUID.setStatus('mandatory')
ctEwvDocSupportUsername = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportUsername.setStatus('mandatory')
ctEwvDocSupportPassword = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvDocSupportPassword.setStatus('mandatory')
ctEwvSystemParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2))
ctEwvAuthScheme = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("basic", 2), ("digest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthScheme.setStatus('mandatory')
ctEwvAuthNonceValidCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4, 1, 2, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctEwvAuthNonceValidCount.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-WEBVIEW-MIB", ctEwvAuthNonceValidCount=ctEwvAuthNonceValidCount, ctEwvAuthScheme=ctEwvAuthScheme, ctEwvDocSupport=ctEwvDocSupport, ctEwvConfiguration=ctEwvConfiguration, ctEwvStatus=ctEwvStatus, ctEwvDocSupportAdmin=ctEwvDocSupportAdmin, ctEwvDocSupportAdminUID=ctEwvDocSupportAdminUID, ctEwvDocSupportLocation=ctEwvDocSupportLocation, ctEwvDocSupportUsername=ctEwvDocSupportUsername, ctWebView=ctWebView, ctEwvSystemParameters=ctEwvSystemParameters, ctEwvDocSupportPassword=ctEwvDocSupportPassword)
